from abc import ABC, abstractmethod
from models.users import (
    CreateUserRequest,
    CreateUserResponse
)
from models.auth import (
    LoginRequest,
    LoginResponse,
    ValidateTokenRequest,
    ValidateTokenResponse
)


class RegistrationInterface(ABC):
    @abstractmethod
    def create_user(self, req: CreateUserRequest) -> CreateUserResponse:
        pass


class AuthenticationInterface(ABC):
    @abstractmethod
    def login(self, req: LoginRequest) -> LoginResponse:
        pass

    @abstractmethod
    def validate_token(self, req: ValidateTokenRequest) -> ValidateTokenResponse:
        pass
