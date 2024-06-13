
from src.controllers.interfaces.pessoa_juridica_lister_controller import PessoaJuridicaListerControllerInterface 
from src.models.sqlite.interfaces.pessoa_juridica_repository import PessoaJuridicaRepositoryInterface
from src.validators.pessoa_juridica_validator import pessoa_juridica_validator
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class PessoaJuridicaListerView(ViewInterface):
    def __init__(self, controller: PessoaJuridicaListerControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        
        body_response = self.__controller.list_pessoas_juridicas()

        return HttpResponse(status_code=201, body=body_response)
    