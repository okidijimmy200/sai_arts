from service.interface.users import RegistrationInterface
from service.interface.storage import UserStorageInterface
from werkzeug.security import generate_password_hash
from models.users import (
    CreateUserRequest,
    CreateUserResponse,
    
)
from models.auth import (
    validate_request
)

class Registration(RegistrationInterface):

    def __init__(self, storage: UserStorageInterface) -> None:
        self.storage = storage

    def create_user(self, req: CreateUserRequest) -> CreateUserResponse:
        try:
            valid, reason = validate_request(req)
            if not valid:
                return CreateUserResponse(400, reason)
            response = self.storage.create_user(CreateUserRequest(
                req.email,
                generate_password_hash(req.password)
            ))
            return CreateUserResponse(response.code, response.response)
        except Exception as e:
            return CreateUserResponse(500, f"failed to sign up: " + f"{type(e).__name__} {str(e)}")