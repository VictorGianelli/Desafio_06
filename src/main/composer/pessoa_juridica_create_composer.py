from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.controllers.pessoa_juridica_creator_controller import PessoaJuridicaCreatorController
from src.views.pessoa_juridica_creator_view import PessoaJuridicaCreatorView

def pessoa_juridica_create_composer():
    model = PessoaJuridicaRepository(db_connection_handler)
    controller = PessoaJuridicaCreatorController(model)
    view = PessoaJuridicaCreatorView(controller)

    return view
