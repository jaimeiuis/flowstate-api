from flask import Flask

from flowstate.blueprints.page import page

from flowstate.extensions import (
    debug_toolbar,
    db,
    jwt,
    marshmallow
)


def create_app(settings_override=None):
    """ Create a Flask app using the factory pattern. """

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    if settings_override:
        app.config.update(settings_override)

    app.register_blueprint(page)
    
    extensions(app)

    return app


def extensions(app):
    """ Mutate the app passed in. """
    debug_toolbar.init_app(app)
    jwt.init_app(app)
    db.init_app(app)
    marshmallow.init_app(app)