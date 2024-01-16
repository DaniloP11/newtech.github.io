from flask import Flask, flash, redirect, render_template, request, session, url_for
from . import productos
import sqlite3
from funciones import getLoginDetails, getCategoryDetails, getProductDetails
import math

@productos.route('/laptops/<pagina>')
def laptops(pagina):
    if 'email' not in session:
        return redirect('/login/')
    # print(f"pagina: {pagina}")
    categoria='laptops'
    datos_categoria, num_categoria=getCategoryDetails(categoria)
    datos, itms_carrito = getLoginDetails(session['email'])
    categoria='laptops'
    #Vamos a paginar (num_paginas) de a n_elementos
    n_elementos=5
    num_paginas=math.ceil(num_categoria/n_elementos)
    lim_inf=0
    lim_sup=n_elementos
    for i in range(1,num_categoria+1):
        if i==int(pagina):
            datos_categoria=datos_categoria[lim_inf:lim_sup]        
        lim_inf+=n_elementos
        lim_sup+=n_elementos
    # print(datos_categoria)
    return render_template("categorias.html", itms_carrito=itms_carrito, categoria=categoria, datos_categoria=datos_categoria, num_paginas=num_paginas)

@productos.route('/consolas/<pagina>')
def consolas(pagina):
    if 'email' not in session:
        return redirect('/login/')
    # print(f"pagina: {pagina}")
    categoria='consolas'
    datos_categoria, num_categoria=getCategoryDetails(categoria)
    datos, itms_carrito = getLoginDetails(session['email'])
    categoria='consolas'
    #Vamos a paginar (num_paginas) de a n_elementos
    n_elementos=5
    num_paginas=math.ceil(num_categoria/n_elementos)
    lim_inf=0
    lim_sup=n_elementos
    for i in range(1,num_categoria+1):
        if i==int(pagina):
            datos_categoria=datos_categoria[lim_inf:lim_sup]        
        lim_inf+=n_elementos
        lim_sup+=n_elementos
    # print(datos_categoria)
    return render_template("categorias.html", itms_carrito=itms_carrito, categoria=categoria, datos_categoria=datos_categoria, num_paginas=num_paginas)

@productos.route('/relojs/<pagina>')
def relojs(pagina):
    if 'email' not in session:
        return redirect('/login/')
    # print(f"pagina: {pagina}")
    categoria='relojs'
    datos_categoria, num_categoria=getCategoryDetails(categoria)
    datos, itms_carrito = getLoginDetails(session['email'])
    categoria='relojs'
    #Vamos a paginar (num_paginas) de a n_elementos
    n_elementos=5
    num_paginas=math.ceil(num_categoria/n_elementos)
    lim_inf=0
    lim_sup=n_elementos
    for i in range(1,num_categoria+1):
        if i==int(pagina):
            datos_categoria=datos_categoria[lim_inf:lim_sup]        
        lim_inf+=n_elementos
        lim_sup+=n_elementos
    # print(datos_categoria)
    return render_template("categorias.html", itms_carrito=itms_carrito, categoria=categoria, datos_categoria=datos_categoria, num_paginas=num_paginas)

@productos.route('/pcescritorio/<pagina>')
def pcescritorio(pagina):
    if 'email' not in session:
        return redirect('/login/')
    # print(f"pagina: {pagina}")
    categoria='pcescritorio'
    datos_categoria, num_categoria=getCategoryDetails(categoria)
    datos, itms_carrito = getLoginDetails(session['email'])
    categoria='pcescritorio'
    #Vamos a paginar (num_paginas) de a n_elementos
    n_elementos=5
    num_paginas=math.ceil(num_categoria/n_elementos)
    lim_inf=0
    lim_sup=n_elementos
    for i in range(1,num_categoria+1):
        if i==int(pagina):
            datos_categoria=datos_categoria[lim_inf:lim_sup]        
        lim_inf+=n_elementos
        lim_sup+=n_elementos
    # print(datos_categoria)
    return render_template("categorias.html", itms_carrito=itms_carrito, categoria=categoria, datos_categoria=datos_categoria, num_paginas=num_paginas)

@productos.route('/celulares/<pagina>')
def celulares(pagina):
    if 'email' not in session:
        return redirect('/login/')
    # print(f"pagina: {pagina}")
    categoria='celulares'
    datos_categoria, num_categoria=getCategoryDetails(categoria)
    datos, itms_carrito = getLoginDetails(session['email'])
    categoria='celulares'
    #Vamos a paginar (num_paginas) de a n_elementos
    n_elementos=5
    num_paginas=math.ceil(num_categoria/n_elementos)
    lim_inf=0
    lim_sup=n_elementos
    for i in range(1,num_categoria+1):
        if i==int(pagina):
            datos_categoria=datos_categoria[lim_inf:lim_sup]        
        lim_inf+=n_elementos
        lim_sup+=n_elementos
    # print(datos_categoria)
    return render_template("categorias.html", itms_carrito=itms_carrito, categoria=categoria, datos_categoria=datos_categoria, num_paginas=num_paginas)

@productos.route('/accesorios/<pagina>')
def accesorios(pagina):
    if 'email' not in session:
        return redirect('/login/')
    # print(f"pagina: {pagina}")
    categoria='accesorios'
    datos_categoria, num_categoria=getCategoryDetails(categoria)
    datos, itms_carrito = getLoginDetails(session['email'])
    categoria='accesorios'
    #Vamos a paginar (num_paginas) de a n_elementos
    n_elementos=5
    num_paginas=math.ceil(num_categoria/n_elementos)
    lim_inf=0
    lim_sup=n_elementos
    for i in range(1,num_categoria+1):
        if i==int(pagina):
            datos_categoria=datos_categoria[lim_inf:lim_sup]        
        lim_inf+=n_elementos
        lim_sup+=n_elementos
    # print(datos_categoria)
    return render_template("categorias.html", itms_carrito=itms_carrito, categoria=categoria, datos_categoria=datos_categoria, num_paginas=num_paginas)

@productos.route('/detalles/')
def detalles():
    if 'email' not in session:
        return redirect('/login/')
    
    productId = request.args.get('productId')
    producto=getProductDetails(productId)

    datos, itms_carrito = getLoginDetails(session['email'])

    return render_template("detalles.html", producto=producto, itms_carrito=itms_carrito)