from abc import ABC, abstractmethod
from models.users import (
    CreateUserRequest,
    CreateUserResponse,
    FindUserRequest,
    FindUserResponse
)


class UserStorageInterface(ABC):
    @abstractmethod
    def create_user(self, req: CreateUserRequest) -> CreateUserResponse:
        pass

    @abstractmethod
    def find_user(self, req: FindUserRequest) -> FindUserResponse:
        pass

# class ArtPieceInterface(ABC):
#     @abstractmethod
    
