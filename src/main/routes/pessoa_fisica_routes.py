from flask import Blueprint, jsonify, request
from src.errors.error_handler import handle_errors
from src.main.composer.pessoa_fisica_composer import pessoa_fisica_composer
from src.views.http_types.http_request import HttpRequest

pessoa_fisica_route_bp = Blueprint("pessoa_fisica_routes", __name__)

@pessoa_fisica_route_bp.route("/pessoa_fisica/create", methods=["POST"])
def create_person():
    try:
        http_request = HttpRequest(body=request.json)
        view = pessoa_fisica_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code

# @pessoa_fisica_route_bp.route("/people", methods=["POST"])
# def create_person():
#     try:
#         http_request = HttpRequest(body=request.json)
#         view = person_creator_composer()

#         http_response = view.handle(http_request)
#         return jsonify(http_response.body), http_response.status_code
#     except Exception as exception:
#         http_response = handle_errors(exception)
#         return jsonify(http_response.body), http_response.status_code

# @pessoa_fisica_route_bp.route("/people/<person_id>", methods=["GET"])
# def find_person(person_id):
#     try:
#         http_request = HttpRequest(param={ "person_id": person_id })
#         view = person_finder_composer()

#         http_response = view.handle(http_request)
#         return jsonify(http_response.body), http_response.status_code
#     except Exception as exception:
#         http_response = handle_errors(exception)
#         return jsonify(http_response.body), http_response.status_code
    
@pessoa_fisica_route_bp.route("/", methods=["POST"])
def init():
    return jsonify({"message": "Hello, World!"})