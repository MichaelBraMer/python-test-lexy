from flask import Blueprint, jsonify
from app.services.status_service import check_status

status_blueprint = Blueprint("status", __name__)

@status_blueprint.route("/", methods=["GET"])
def get_status():
    return jsonify(check_status())