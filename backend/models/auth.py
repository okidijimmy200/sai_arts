from dataclasses import dataclass
from typing import Tuple


@dataclass
class LoginRequest:
    email: str
    password: str


@dataclass
class LoginResponse:
    code: int
    response: str
    token: str


@dataclass
class ValidateTokenRequest:
    token: str


@dataclass
class ValidateTokenResponse:
    code: int
    reason: str
    user_id: str


def validate_request(instance) -> Tuple[bool, str]:
    for key, value in instance.__dict__.items():
        if isinstance(value, str) and value == "":
            return False, f"{key} is required"
        if isinstance(value, int) and value == 0:
            return False, f"{key} is required"
    return True, ""
