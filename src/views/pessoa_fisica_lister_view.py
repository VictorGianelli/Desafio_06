
from src.controllers.interfaces.pessoa_fisica_lister_controller import PessoaFisicaListerControllerInterface 
from src.models.sqlite.interfaces.pessoa_fisica_repository import PessoaFisicaRepositoryInterface
from src.validators.pessoa_fisica_validator import pessoa_fisica_validator
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class PessoaFisicaListerView(ViewInterface):
    def __init__(self, controller: PessoaFisicaListerControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        
        body_response = self.__controller.list_pessoas_fisicas()

        return HttpResponse(status_code=201, body=body_response)
    