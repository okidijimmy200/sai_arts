from flask import request
from flask import Blueprint, jsonify
import server.http.server as server
from models.auth import (
    LoginRequest,
    LoginResponse
)

auth_api = Blueprint('auth_api', __name__)


@auth_api.route('/login', methods=['POST'])
def login():
    try:
        data: dict = request.get_json()

        req = LoginRequest(
            data.get('email'),
            data.get('password')
        )

        response = server.auth_service.login(req)

        reason = {
            "code": response.code,
            "reason": response.response,
            "token": response.token
        }
        return jsonify(reason)
    except Exception as e:
        return LoginResponse(500, f"-Error " + f"{type(e).__name__} {str(e)}", "")
