from dataclasses import dataclass

@dataclass
class User:
    id: str
    email: str
    password: str

@dataclass
class CreateUserRequest:
    email: str
    password: str

@dataclass
class CreateUserResponse:
    code: int
    response: str

@dataclass
class FindUserRequest:
    email: str

@dataclass
class FindUserResponse:
    code: int
    reason: str
    user: object


