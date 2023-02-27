from pydantic import BaseModel
from pydantic import ValidationError
from errors import HttpError

class CreateElement(BaseModel):

    title: str
    password: str
    owner: str

    def validate_create_element(json_data):
        try:
            user_shema = CreateElement(**json_data)
            return user_shema.dict()
        except ValidationError as er:
            raise HttpError(status_code=400, message=er.errors())



