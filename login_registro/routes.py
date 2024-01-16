from flask import Flask, flash, redirect, render_template, request, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from login_registro import login_registro
import sqlite3

def esta_registrado(email, password):
    #Inicializamos un mensaje falso
    msg='No se encontró el correo ingresado'

    #Buscaremos si el correo se encuentra registrado
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('SELECT email, password FROM usuarios')
    data = cur.fetchall()
    
    #Comparamos si el correo esta en la consulta sql
    for row in data:
        if row[0] == email:
            #Si el correo se encuentra registrado cambiamos el valor de la variable
            msg='Registrado'
            if row[1] == password:
                #Ahora comparamos si la contraseña es la misma registrada
                msg='Password correcto'
            else:
                msg='La contraseña ingresada no es correcta'
    return msg

def consulta_por_email(email):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM usuarios WHERE email=?',(email,))
    data = cur.fetchone()
    return data

@login_registro.route('/login/')
def login():
    return render_template('login.html')

@login_registro.route('/iniciar_sesion', methods = ['POST', 'GET'])
def iniciar_sesion():
    if request.method == 'POST':
        #Obtenemos los datos del formulario
        email = request.form['email']
        password = request.form['password']
        
        #Verificamos si los campos estan llenos
        if email=='' or password=='':
            flash("Por favor, complete todos los campos del formulario", "danger")
            return render_template('login.html')
        ##Verificacmos si el correo está registrado, implementamos la funcion creada al inicio
        # Verificamos si el correo está registrado
        data = consulta_por_email(email)
        if data:
            if data and check_password_hash(data[5], password): # data[5] es el hash de la contraseña en la base de datos
                session['email'] = email
                session['id'] = data[0]
                session['nombres'] = data[1]
                session['apellidos'] = data[2]
                session['celular'] = data[3]
                session['password'] = data[5]
                session['tipoUser'] = data[6]
                print(session)
                if session['tipoUser'] == 'usuario':
                    return redirect('/')
                else:
                    return redirect('/admin')
            else:
                flash("La contraseña ingresada no es correcta", "danger")
        else:
            flash("El correo ingresado no está registrado", "danger")

    return render_template('login.html')

@login_registro.route('/registro/')
def registro():
    return render_template('registro.html')

@login_registro.route('/registro_usuario', methods = ['POST', 'GET'])
def registro_usuario():
    if request.method == 'POST':
        #Obtenemos los datos del formulario
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        celular = request.form['celular']

        #Verificamos si los campos estan llenos
        if email=='' or password=='' or nombres=='' or apellidos=='' or celular=='':
            flash("Por favor, complete todos los campos del formulario", "danger")
            return render_template('registro.html')
        
        # Verificamos si las contraseñas coinciden
        if password != confirm_password:
            flash("Las contraseñas no coinciden", "danger")
            return render_template('registro.html')
        # Hasheamos la contraseña antes de almacenarla
        hashed_password = generate_password_hash(password)

        ##Verificacmos si el correo está registrado, implementamos la funcion creada al inicio
        msg=esta_registrado(email, password)
        if msg=='Registrado' or msg=='Password correcto' or msg=='La contraseña ingresada no es correcta': #si esta registrado
            flash("El correo ingresado ya está registrado,\n ingrese otro nuevamente", "danger")
            return render_template('registro.html')
        else: #
            session['email'] = email
            try:           
                con=sqlite3.connect("database.db")
                cur=con.cursor()
                cur.execute("INSERT INTO usuarios(nombres,apellidos,celular,email,password,tipoUser) VALUES (?,?,?,?,?,?)",
                        (nombres, apellidos, celular, email, hashed_password, 'usuario'))
                con.commit()
                datos=consulta_por_email(email)
                session['id']=datos[0]
                session['nombres']=datos[1]
                session['apellidos']=datos[2]
                session['celular']=datos[3]
                session['password']=datos[5]
                session['tipoUser']=datos[6]
                print(session)
                if session['tipoUser']=='usuario':
                    flash("Inicio de sesion exitoso, ahora puedes ver nuestros productos","success")
                    return redirect('/')
                else:
                    return redirect('/admin')
            except:
                flash("Error en la operación de inserción","danger")
                return render_template('registro.html')
            

@login_registro.route('/perfil/')
def perfil():
    return render_template('perfil.html')

@login_registro.route("/actualizar_perfil", methods=['POST'])
def actualizar_perfil():
    try:
        # Obtener datos del formulario
        current_password = request.form['current_password']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        nuevos_nombres = request.form['nombres']
        nuevos_apellidos = request.form['apellidos']
        nuevo_celular = request.form['celular']
        nuevo_email = request.form['email']

        # Conectar a la base de datos
        con = sqlite3.connect("database.db")
        cur = con.cursor()

        # Obtener información del usuario actual
        user = cur.execute("SELECT * FROM usuarios WHERE userId=?", (session['id'],)).fetchone()

        # Verificar si la contraseña actual coincide
        if not check_password_hash(user[5], current_password):  
            flash("La contraseña actual ingresada no coincide con la contraseña almacenada.", "danger")
            con.close()
            return redirect('/perfil')

        # Validar que las contraseñas coincidan si se están actualizando
        if password != '' and password != confirm_password:
            flash("La nueva contraseña y la confirmación de la contraseña no coinciden.", "danger")
            con.close()
            return redirect('/perfil')

        # Actualizar datos en la base de datos
        try:
            cur.execute("UPDATE usuarios SET nombres=?, apellidos=?, celular=?, email=?, password=? WHERE userId=?",
                        (nuevos_nombres, nuevos_apellidos, nuevo_celular, nuevo_email, generate_password_hash(password, method='pbkdf2:sha256'), session['id']))
            con.commit()

            # Actualizar datos en la sesión
            session['nombres'] = nuevos_nombres
            session['apellidos'] = nuevos_apellidos
            session['celular'] = nuevo_celular
            session['email'] = nuevo_email

            con.close()
            flash("Perfil actualizado exitosamente", "success")
            return redirect('/perfil')
        except Exception as e:
            flash(f"Error en la actualización del perfil: {str(e)}", "danger")
            con.close()
            return redirect('/perfil')
    except Exception as e:
        flash(f"Error en la actualización del perfil: {str(e)}", "danger")
        return redirect('/perfil')


@login_registro.route("/logout")
def logout():
    session.clear()
    return redirect("/")
