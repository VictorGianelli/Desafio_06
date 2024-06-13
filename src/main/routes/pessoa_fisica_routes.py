from flask import Blueprint, jsonify, request
from src.errors.error_handler import handle_errors
from src.main.composer.pessoa_fisica_create_composer import pessoa_fisica_create_composer
from src.main.composer.pessoa_fisica_lister_composer import pessoa_fisica_lister_composer
from src.views.http_types.http_request import HttpRequest

pessoa_fisica_route_bp = Blueprint("pessoa_fisica_routes", __name__)

@pessoa_fisica_route_bp.route("/pessoa_fisica/create", methods=["POST"])
def create_person():
    try:
        http_request = HttpRequest(body=request.json)
        view = pessoa_fisica_create_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
    
@pessoa_fisica_route_bp.route("/pessoa_fisica/list", methods=["GET"])
def list_pessoas_fisicas():
    try:
        http_request = HttpRequest()
        view = pessoa_fisica_lister_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
    
@pessoa_fisica_route_bp.route("/", methods=["POST"])
def init():
    return jsonify({"message": "Hello, World!"})