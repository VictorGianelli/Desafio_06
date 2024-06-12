from pydantic import BaseModel, constr, ValidationError
from src.views.http_types.http_request import HttpRequest
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def pessoa_fisica_validator(http_request: HttpRequest) -> None:

    class BodyData(BaseModel):
        renda_mensal: int
        idade: int
        nome_completo: constr(min_length=1) # type: ignore
        celular: constr(min_length=9) # type: ignore
        email: str
        categoria: str
        saldo: int
    
    try:
        BodyData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntityError(e.errors()) from e
    