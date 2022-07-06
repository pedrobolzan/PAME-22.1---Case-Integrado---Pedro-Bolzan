from flask import Flask
from .config import Config
from .extensions import db, migrate

from app.agendamento.routes import agendamento_api
from app.checklist.routes import checklist_api

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(agendamento_api)
    app.register_blueprint(checklist_api)
    
    return app