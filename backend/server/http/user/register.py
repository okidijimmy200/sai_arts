from flask import request
from flask import Blueprint, jsonify
import server.http.server as server
from models.users import (
    CreateUserRequest,
    CreateUserResponse
)

registration_api = Blueprint('registration_api', __name__)


@registration_api.route('/signup', methods=['POST'])
def signup():
    try:
        data: dict = request.get_json()
        req = CreateUserRequest(
            data.get('email'),
            data.get('password')
        )
        response = server.reg_service.create_user(req)

        response = {
            "code": response.code,
            "reason": response.response
        }
        return jsonify(response)
    except Exception as e:
        return CreateUserResponse(500,  f"-Error " + f"{type(e).__name__} {str(e)}")
