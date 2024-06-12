from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.cliente_repository import ClienteRepositoryInterface
from src.controllers.pessoa_fisica_creator_controller import PersonCreatorController
from src.views.pessoa_fisica_creator_view import PersonCreatorView

def pessoa_fisica_composer():
    model = ClienteRepositoryInterface(db_connection_handler)
    controller = PersonCreatorController(model)
    view = PersonCreatorView(controller)

    return view
