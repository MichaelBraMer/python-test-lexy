from flask import Blueprint, jsonify
from app.services.leads_service import fetch_data

leads_blueprint = Blueprint("leads", __name__)

@leads_blueprint.route("/", methods=["GET"])
def get_crm_data():
    return jsonify(fetch_data())
