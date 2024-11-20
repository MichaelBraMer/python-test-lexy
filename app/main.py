from flask import Flask
from app.controllers.status_controller import status_blueprint
from app.controllers.leads_controller import leads_blueprint
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)

    load_dotenv()
    
    # Registrar blueprints
    app.register_blueprint(status_blueprint, url_prefix="/status")
    app.register_blueprint(leads_blueprint, url_prefix="/leads")
    
    return app