from flask import Blueprint, jsonify, request
from src.errors.error_handler import handle_errors
from src.main.composer.pessoa_juridica_create_composer import pessoa_juridica_create_composer
from src.main.composer.pessoa_juridica_lister_composer import pessoa_juridica_lister_composer
from src.views.http_types.http_request import HttpRequest

pessoa_juridica_route_bp = Blueprint("pessoa_juridica_routes", __name__)

@pessoa_juridica_route_bp.route("/pessoa_juridica/create", methods=["POST"])
def create_person():
    try:
        http_request = HttpRequest(body=request.json)
        view = pessoa_juridica_create_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
    
@pessoa_juridica_route_bp.route("/pessoa_juridica/list", methods=["GET"])
def list_pessoas_juridicas():
    try:
        http_request = HttpRequest()
        view = pessoa_juridica_lister_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
    
