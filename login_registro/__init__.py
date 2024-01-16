from flask import Blueprint

login_registro = Blueprint('login_registro', __name__, template_folder='templates')
from . import routes