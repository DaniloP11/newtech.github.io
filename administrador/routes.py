import os
from flask import Flask, flash, redirect, render_template, request, session, url_for
from . import administrador
import sqlite3
from funciones import getLoginDetails, getCategoryDetails, getProductDetails, getUsers, all_compras
from werkzeug.utils import secure_filename


@administrador.route('/admin')
def admin():
    if 'email' not in session:
        return redirect('/login/')
    elif session['tipoUser'] != 'administrador':
        return redirect('/')
    else:
        administradores=getUsers('administrador')
        usuarios=getUsers('usuario')
        return render_template('index_admin.html', administradores=administradores, usuarios=usuarios)
    
@administrador.route('/productos_admin/<cat>')
def productos_admin(cat):
    if 'email' not in session:
        return redirect('/login/')
    elif session['tipoUser'] != 'administrador':
        return redirect('/')
    else:
        # cat=str(cat)
        laptops,numero=getCategoryDetails('laptops')
        consolas,numero=getCategoryDetails('consolas')
        relojs,numero=getCategoryDetails('relojs')
        pcescritorio,numero=getCategoryDetails('pcescritorio')
        celulares,numero=getCategoryDetails('celulares')
        accesorios,numero=getCategoryDetails('accesorios')
        # print(laptops)
        if cat=='laptops':
            return render_template('productos_admin.html', categoria=laptops)
        if cat=='consolas':
            return render_template('productos_admin.html', categoria=consolas)
        if cat=='relojs':
            return render_template('productos_admin.html', categoria=relojs)
        if cat=='pcescritorio':
            return render_template('productos_admin.html', categoria=pcescritorio)
        if cat=='celulares':
            return render_template('productos_admin.html', categoria=celulares)
        if cat=='accesorios':
            return render_template('productos_admin.html', categoria=accesorios)
        

@administrador.route('/detalles_admin/')
def detalles_admin():
    if 'email' not in session:
        return redirect('/login/')
    elif session['tipoUser'] != 'administrador':
        return redirect('/')
    
    productId = request.args.get('productId')
    producto=getProductDetails(productId)

    return render_template("detalles_admin.html", producto=producto)

@administrador.route('/editar', methods = ['POST', 'GET'])
def editar():
    if 'email' not in session:
        return redirect('/login/')
    elif session['tipoUser'] != 'administrador':
        return redirect('/')
    
    if request.method == 'POST':
        #Obtenemos los datos del formulario
        productId=int(request.form['productId'])
        categoria=request.form['categoria']
        producto=getProductDetails(productId)

        nombre = request.form['nombre']
        precio = float(request.form['precio'])
        descripcion = request.form['descripcion']
        cantidad = int(request.form['cantidad'])
        imagen = request.form['imagen']
        #Uploading image procedure
        imagen2 = request.files['imagen2']
        upload='static/assets/img'
        if imagen=='':
            if not imagen2:
                flash("Debe seleccionar una imagen","danger")
                return redirect(f"/detalles_admin?productId={productId}")
            else:
                filename = secure_filename(imagen2.filename)
                imagen2.save(os.path.join(upload, filename))
                nombre_imagen=f"/static/assets/img/{filename}"
        else:
            nombre_imagen=imagen

        with sqlite3.connect('database.db') as con:
            try:
                cur = con.cursor()
                cur.execute('UPDATE productos SET nombre = ?, precio = ?, descripcion = ?, imagen = ?, cantidad = ?, categoria = ? WHERE productId=?', (nombre, precio, descripcion, nombre_imagen, cantidad, categoria, productId))
                con.commit()
                flash("Se modificó exitosamente el producto", "success")
                return redirect(f"/productos_admin/{categoria}")
            except Exception as e:
                con.rollback()
                flash(f"Error occured {e}", "danger")
                
        con.close()

        # print(productId, categoria,nombre,precio,descripcion,cantidad,nombre_imagen)
        return redirect(f"/detalles_admin?productId={productId}")
        
@administrador.route('/delete_admin/')##########################
def delete_admin():
    if 'email' not in session:
        return redirect('/login/')
    elif session['tipoUser'] != 'administrador':
        return redirect('/')
    
    productId = request.args.get('productId')
    producto=getProductDetails(productId)
    categoria=producto[6]
    with sqlite3.connect('database.db') as conn:
        try:
            cur = conn.cursor()
            cur.execute('DELETE FROM productos WHERE productID = ?', (productId, ))
            conn.commit()
            flash(f"Se eliminó correctamente en la categoria {categoria}", "success")
        except Exception as e:
            conn.rollback()
            flash(f"Ocurrió un error {e}", "danger")
    conn.close()

    return redirect(f"/productos_admin/{categoria}")

@administrador.route('/agregar_producto/')
def agregar_producto():
    if 'email' not in session:
        return redirect('/login/')
    elif session['tipoUser'] != 'administrador':
        return redirect('/')

    return render_template("registrar_productos.html")

@administrador.route("/registrar_producto", methods=["GET", "POST"])
def registrar_producto():
    if 'email' not in session:
        return redirect('/login/')
    elif session['tipoUser'] != 'administrador':
        return redirect('/')
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = float(request.form['precio'])
        descripcion = request.form['descripcion']
        cantidad = int(request.form['cantidad'])
        categoria = request.form['categoria']
        imagen = request.form['imagen']
        #Uploading image procedure
        imagen2 = request.files['imagen2']
        upload='static/assets/img'
        if imagen=='':
            if not imagen2:
                flash("Debe seleccionar una imagen","danger")
                return redirect("/agregar_producto")
            else:
                filename = secure_filename(imagen2.filename)
                imagen2.save(os.path.join(upload, filename))
                nombre_imagen=f"/static/assets/img/{filename}"
        else:
            nombre_imagen=imagen
        # print(categoria,nombre,precio,descripcion,cantidad,nombre_imagen)

        with sqlite3.connect('database.db') as conn:
            try:
                cur = conn.cursor()
                cur.execute('''INSERT INTO productos (nombre, precio, descripcion, imagen, cantidad, categoria) VALUES (?, ?, ?, ?, ?, ?)''', (nombre, precio, descripcion, nombre_imagen, cantidad, categoria))
                conn.commit()
                flash(f"Se agregó correctamente en la categoria {categoria}", "success")
                return redirect(f"/productos_admin/{categoria}")

            except Exception as e:
                flash(f"Ocurrio un error {e}", "danger")
                conn.rollback()
        conn.close()
        return redirect("/agregar_producto")
    


@administrador.route('/ver_compras')
def ver_compras():
    if 'email' not in session:
        return redirect('/login/')
    elif session['tipoUser'] != 'administrador':
        return redirect('/')
    compras_user=all_compras()
    
    
   
    return render_template('mostrar_compras_admin.html', compras_user=compras_user)
