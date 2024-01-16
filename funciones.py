import sqlite3

def getLoginDetails(email):
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM usuarios WHERE email = ?", (email, ))
        data = cur.fetchone()

        userId=data[0]
        cur.execute("SELECT count(*) FROM kart WHERE userId = ?", (userId, ))
        noItems = cur.fetchone()[0]
    conn.close()
    # print(data, noItems)

    return (data, noItems)

def getCategoryDetails(categoria):
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM productos WHERE categoria = ?", (categoria, ))
        data = cur.fetchall()
        cur.execute("SELECT count(*) FROM productos WHERE categoria = ?", (categoria, ))
        noItems = cur.fetchone()[0]
    conn.close()
    return (data, noItems)

def getProductDetails(id_producto):
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM productos WHERE productId = ?", (id_producto, ))
        data = cur.fetchone()
        
    conn.close()
    # print(data)
    return (data)

def getCartDetails(userId):
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT kartId, productos.productId, productos.nombre, productos.precio,productos.descripcion, productos.imagen, productos.categoria, kart.productCantidad, kart.precio FROM productos, kart WHERE productos.productId = kart.productId AND kart.userId = ?", (userId, ))
        data = cur.fetchall()
    conn.close()
    # print(data)

    return (data)

def getUsers(tipo):
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM usuarios WHERE tipoUser = ?", (tipo, ))
        data = cur.fetchall()
    conn.close()
    return (data)

def getCompraDetails(userId):
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT compras.factura, compras.lista_productos, compras.cantidad_productos, compras.total, compras.fecha, compras.direccion, compras.metodo_pago, productos.nombre, productos.descripcion, productos.categoria FROM compras, productos WHERE compras.lista_productos=productos.productId AND compras.userId = ?", (userId, ))
        data = cur.fetchall()
    conn.close()
    # print(data)

    return (data)

def all_compras():
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT compras.factura, compras.lista_productos, compras.cantidad_productos, compras.total, compras.fecha, compras.direccion, compras.metodo_pago, productos.nombre, productos.descripcion, productos.categoria, compras.userId, usuarios.nombres, usuarios.apellidos, usuarios.email, usuarios.celular FROM compras, productos, usuarios WHERE compras.lista_productos=productos.productId AND compras.userId=usuarios.userId")
        data = cur.fetchall()
    conn.close()
    # print(data)

    return (data)

