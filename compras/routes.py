from flask_mail import Mail, Message
from datetime import datetime
from flask import Flask, flash, redirect, render_template, request, session, url_for
from . import compras
import sqlite3
from funciones import getLoginDetails, getProductDetails, getCartDetails, getCompraDetails
from config import config

app = Flask(__name__)
mail = Mail()  


@compras.route('/comprar/')
def comprar():
    if 'email' not in session:
        return redirect('/login/')  
    usuario,itms_carrito=getLoginDetails(session['email'])
    userId=usuario[0]
    return render_template('comprar.html', itms_carrito=itms_carrito)

@compras.route('/registrar_compra', methods=['POST', 'GET'])
def registrar_compra():
    if 'email' not in session:
        return redirect('/login/')

    usuario, itms_carrito = getLoginDetails(session['email'])
    userId = usuario[0]

    # Configurar Flask-Mail
    app.config.from_object(config.get("default", "config.ProductionConfig"))
    mail.init_app(app)

    datos_cliente = None  # Inicializa datos_cliente

    if request.method == 'POST':
        # Obtener datos del formulario
        direccion = request.form.get('direccion')
        met_pago = request.form.get('pago')

        kart = getCartDetails(userId)
        precio_total = 0
        lista_productos = ''
        lista_cantidad = ''

        # Obtener el número de factura
        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT MAX(factura) FROM compras")
            ultima_factura = cur.fetchone()[0]

            factura = 1 if ultima_factura is None else int(ultima_factura) + 1

        # Realizar la transacción de compra
        with sqlite3.connect('database.db') as conn:
            try:
                cur = conn.cursor()
                for product in kart:
                    precio_total += product[3]
                    cur.execute(
                        "INSERT INTO compras (userId, factura, lista_productos, cantidad_productos, total, fecha, direccion, metodo_pago) VALUES (?, ?, ?, ?, ?, datetime('now','localtime'), ?, ?)",
                        (userId, factura, product[1], product[7], product[3] * product[7], direccion, met_pago))

                # Obtener información del cliente
                nombre_usuario = f"{usuario[1]} {usuario[2]}"
                celular = usuario[3]
                email = usuario[4]
                datos_cliente = {
                    'nombre_usuario': nombre_usuario,
                    'celular': celular,
                    'email': email,
                    'direccion': direccion,
                    'metodo_pago': met_pago,
                    'fecha': datetime.now().strftime('%Y-%m-%d'),
                }

                # Enviar correo electrónico
                enviar_correo(email, factura, precio_total, kart, datos_cliente)
                conn.commit()

                flash("Se realizó su compra exitosamente", "success")
                return redirect(f"/mostrar_factura?factura={factura}&precio_total={precio_total}")

            except Exception as e:
                conn.rollback()
                flash(f"No se pudo realizar la compra: {e}", "danger")

    return redirect('/comprar')

        
@compras.route('/mostrar_factura')
def mostrar():
    if 'email' not in session:
        return redirect('/login/')
    factura = request.args.get('factura')
    precio_total = request.args.get('precio_total')
    usuario, itms_carrito = getLoginDetails(session['email'])
    userId = usuario[0]
    nombre_usuario = f"{usuario[1]} {usuario[2]}"
    celular = usuario[3]
    email = usuario[4]
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT kartId, productos.productId, productos.nombre, productos.precio, productos.imagen, kart.productCantidad, kart.precio, productos.categoria, productos.descripcion FROM productos, kart WHERE productos.productId = kart.productId AND kart.userId = ?", (userId, ))
        productos = cur.fetchall()
        cur.execute("SELECT * FROM compras WHERE factura=?", (factura,))
        info = cur.fetchone()
        compraId = factura
        fecha = info[6]
        direccion = info[7]
        met_pago = info[8]

        cur.execute("DELETE FROM kart WHERE userId=?", (userId,))
        conn.commit()

        # Obtener la lista de cantidades
        lista_cantidad = [product[5] for product in productos]

    conn.close()
    precio_total = 0
    for product in productos:
        precio_total += product[6]

    datos_cliente = [nombre_usuario, celular, email, direccion, met_pago, fecha, precio_total, compraId]

    return render_template('mostrar_factura.html', itms_carrito=itms_carrito, productos=productos, datos_cliente=datos_cliente, lista_cantidad=lista_cantidad)


@compras.route('/mis_compras')
def mis_compras():
    if 'email' not in session:
        return redirect('/login/')
    usuario,itms_carrito=getLoginDetails(session['email'])
    userId=usuario[0]
    nombre_usuario=f"{usuario[1]} {usuario[2]}"
    celular=usuario[3]
    email=usuario[4]
    compras_user=getCompraDetails(userId)
    
    # print(compras_user)
    return render_template('mostrar_compras.html', itms_carrito=itms_carrito, compras_user=compras_user)


def enviar_correo(destinatario, factura, precio_total, productos, datos_cliente):
    # Crear el cuerpo del correo con formato profesional
    cuerpo_correo = f'''
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background-color: #f4f4f4;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
                background-color: #fff;
                padding: 20px;
                border-radius: 5px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                border: 1px solid #ddd; /* Borde para simular hoja de bloc */
            }}
            h1 {{
                color: purple;
                text-align: center;
            }}
            h2, h3 {{
                color: #333;
                font-weight: bold;
            }}
            ul {{
                list-style-type: none;
                padding: 0;
            }}
            li {{
                margin-bottom: 10px;
            }}
            strong {{
                color: #000;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>NEWTECH - Confirmación de compra</h1>

            <h3>Se ha realizado una compra con la factura No. <strong>{factura}</strong>.</h3>

            <!-- Agregar detalles del cliente al cuerpo del correo -->
            <h2>Detalles del cliente:</h2>
            <ul>
    '''
    for key, value in datos_cliente.items():
        cuerpo_correo += f'''
            <li><strong>{key.capitalize()}:</strong> <strong>{value}</strong></li>
        '''
    cuerpo_correo += '''
            </ul>


            <h2>Detalles de la compra:</h2>
            <ul>
    '''

    # Inicializar la variable para almacenar el precio total de la compra
    precio_total_compra = 0

    for product in productos:
        # Calcular el subtotal para cada producto
        subtotal_producto = product[3] * product[7]  # Precio Unitario * Cantidad

        # Sumar el subtotal al precio total de la compra
        precio_total_compra += subtotal_producto

        cuerpo_correo += f'''
            <li><strong>Producto:</strong> {product[2]},<br>
                <strong>Precio Unitario:</strong> ${product[3]},<br>
                <strong>Cantidad:</strong> {product[7]},<br>
                <strong>Subtotal:</strong> ${subtotal_producto},<br>
                <strong>Detalles:</strong> {product[4]},<br>              
                <strong>Mira tu producto:</strong> {product[5]}</li>
        '''

    # Mostrar el precio total de la compra en el correo
    cuerpo_correo += f'''
            </ul>
            <h3><strong>Valor de envío:</strong> $20000</h3>
            <h2><strong>Total de la compra:</strong> ${precio_total_compra + 20000}</h2>
            <h1>Gracias Por preferirnos.</h1>

        </div>
    </body>
    </html>
    '''

    # Crear el mensaje y enviar el correo
    msg = Message('Confirmación de compra - NEWTECH', recipients=[destinatario])
    msg.html = cuerpo_correo

    mail.send(msg)  # Asegúrate de tener configurada la variable 'mail' correctamente










