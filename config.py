import os

from database.config import get_database_uri


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = get_database_uri()

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        from sassutils.wsgi import SassMiddleware

        app_file = os.environ.get('FLASK_APP').split('.')[0]

        app.wsgi_app = SassMiddleware(app.wsgi_app, {
            app_file: ('static/scss', 'static/css', '/static/css')
        })


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = get_database_uri()


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
