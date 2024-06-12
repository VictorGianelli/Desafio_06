from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.cliente_repository import PessoaFisicaRepository
from src.controllers.person_finder_controller import PersonFinderController
from src.views.person_finder_view import PersonFinderView

def person_finder_composer():
    model = PessoaFisicaRepository(db_connection_handler)
    controller = PersonFinderController(model)
    view = PersonFinderView(controller)

    return view
