from flask import Flask
from service.interface.users import RegistrationInterface
from server.http.user.register import registration_api
from server.http.auth.auth import auth_api
from service.interface.users import AuthenticationInterface


reg_service: RegistrationInterface
auth_service: AuthenticationInterface


def get_app(
    reg: RegistrationInterface,
    auth: AuthenticationInterface
):
    app = Flask(__name__)

    global reg_service, auth_service
    reg_service = reg
    auth_service = auth

    app.register_blueprint(registration_api, name='register')
    app.register_blueprint(auth_api, name='auth')

    return app
