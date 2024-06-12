
from src.controllers.interfaces.pessoa_fisica_creator_controller import PessoaFisicaCreatorControllerInterface
from src.validators.pessoa_fisica_validator import pessoa_fisica_validator
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class PessoaFisicaCreatorView(ViewInterface):
    def __init__(self, controller: PessoaFisicaCreatorControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pessoa_fisica_validator(http_request)
        
        person_info = http_request.body
        body_response = self.__controller.create(person_info)

        return HttpResponse(status_code=201, body=body_response)
    