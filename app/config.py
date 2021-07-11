from app.sensive import Sensive as sensive

class Config:
    SQLALCHEMY_DATABASE_URI = sensive.SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = sensive.SQLALCHEMY_TRACK_MODIFICATIONS
    JSON_SORT_KEYS = sensive.JSON_SORT_KEYS

    #Toda a aplicação tem chaves que não devem ser visíveis, como a do SendGrid

    MAIL_SERVER = sensive.MAIL_SERVER
    MAIL_PORT = sensive.MAIL_PORT
    MAIL_USERNAME = sensive.MAIL_USERNAME
    MAIL_PASSWORD = sensive.MAIL_PASSWORD
    MAIL_USE_TLS = sensive.MAIL_USE_TLS
    MAIL_USE_SSL = sensive.MAIL_USE_SSL


    