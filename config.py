import os

class Config:
    SECRET_KEY = 'clave_secreta'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True  # Cambiado a False
    MAIL_USE_SSL = False   # Nueva línea
    MAIL_USERNAME = 'danilo.paguay@gmail.com'
    MAIL_PASSWORD = 'vzqy gxhf ahwp dqph'
    MAIL_DEFAULT_SENDER = 'danilo.paguay@gmail.com'

class Development(Config):
    DEBUG = True

class Testing(Config):
    TESTING = True

class Production(Config):
    pass

config = {
    'development': Development,
    'testing': Testing,
    'production': Production,
    'default': Development
}
