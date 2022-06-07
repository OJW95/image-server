from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_envvar('APP_CONFIG_FILE')

    # ORM
    db.init_app(app)

    #migrate.init_app(app, db)
    from. import models

    # blueprint
    from .views import main_views, image_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(image_views.bp)
    app.register_blueprint(auth_views.bp)

    #filter
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    return app