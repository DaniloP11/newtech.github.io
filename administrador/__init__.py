from flask import Blueprint

administrador = Blueprint('administrador', __name__, template_folder='templates')
from . import routes