import os
import jwt
from service.interface.users import AuthenticationInterface
from service.interface.storage import UserStorageInterface
from werkzeug.security import check_password_hash
from models.auth import (
    LoginRequest,
    LoginResponse,
    ValidateTokenRequest,
    ValidateTokenResponse,
)
from models.users import FindUserRequest


class Authentication(AuthenticationInterface):
    def __init__(self, storage: UserStorageInterface) -> None:
        self.storage = storage

    def login(self, req: LoginRequest) -> LoginResponse:
        try:
            response = self.storage.find_user(FindUserRequest(req.email))
            print(response)
            if response.code != 200 and response.code != 201:
                return LoginResponse(response.code, response.reason, None)
            token = jwt.encode({"id": response.user.id, "email": response.user.email},
                               os.environ["SECRET_KEY"], algorithm="HS256")

            if check_password_hash(response.user.password, req.password):
                return LoginResponse(
                    response.code,
                    response.reason,
                    token
                )
        except Exception as e:
            return LoginResponse(500, f"{type(e).__name__} {str(e)}", None)

    def validate_token(self, req: ValidateTokenRequest) -> ValidateTokenResponse:
        return super().validate_token(req)
