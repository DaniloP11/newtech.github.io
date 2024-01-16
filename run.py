from flask import Flask, render_template, abort
#importamos la libreria para logs
import logging
from config import config
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(config.get("default", "config.ProductionConfig"))

# Configuración de Flask-Mail
mail = Mail()
mail.init_app(app)

# Configuración de los Blueprints
from login_registro import login_registro
from productos import productos
from carrito import carrito
from administrador import administrador
from compras import compras

app.register_blueprint(login_registro)
app.register_blueprint(productos)
app.register_blueprint(carrito)
app.register_blueprint(administrador)
app.register_blueprint(compras)

# Configuración de logs
logging.basicConfig(filename='app.log', level=logging.DEBUG)

# Rutas principales
@app.route('/')
def inicio():
    logging.info('Ruta principal accesada.')
    return render_template("index.html")

error_codes = [
    400, 401, 403, 404, 405, 406, 408, 409, 410, 411, 412, 413, 414, 415,
    416, 417, 418, 422, 428, 429, 431, 451, 500, 501, 502, 503, 504, 505
]

def custom_error_handler(error):
    code = getattr(error, 'code', 500)
    logging.error(f'Error {code}: {error.description}')

    if code == 400:
        return render_template('error_400.html', error=error), code
    elif code == 500:
        return render_template('error_500.html', error=error), code
    elif code == 502:
        return render_template('error_502.html', error=error), code
    elif code == 503:
        return render_template('error_503.html', error=error), code
    else:
        return render_template('error.html', error=error), code

for code in error_codes:
    app.register_error_handler(code, custom_error_handler)

# Rutas de error con logs
@app.route('/error_404')
def error_404():
    logging.error('Error 404: Página no encontrada.')
    abort(404)

@app.route('/error_400')
def error_400():
    logging.error('Error 400: Solicitud incorrecta.')
    abort(400)

@app.route('/error_500')
def error_500():
    logging.error('Error 500: Error interno del servidor.')
    abort(500)

@app.route('/error_502')
def error_502():
    logging.error('Error 502: Puerta de enlace incorrecta.')
    abort(502)

@app.route('/error_503')
def error_503():
    logging.error('Error 503: Servicio no disponible.')
    abort(503)

if __name__ == '__main__':
    app.run(port=5000)
