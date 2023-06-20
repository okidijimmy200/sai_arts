import json
from bson import json_util
from service.interface.storage import UserStorageInterface
from models.users import (
    User,
    CreateUserRequest,
    CreateUserResponse,
    FindUserRequest,
    FindUserResponse
)


class MongoStorage(UserStorageInterface):
    def __init__(self, mongo_conn, database, collection) -> None:
        self.client = mongo_conn

        cursor = self.client[database]
        self.collection = cursor[collection]

    '''find user'''

    def find_user(self, req: FindUserRequest) -> FindUserResponse:
        try:
            user = self.collection.find_one({"email": f"{req.email}"})
            new_user = json.loads(json_util.dumps(user))

            if user is None:
                return FindUserResponse(404, "User not found", None)
            return FindUserResponse(200, "Successfully Logged In", User(new_user['_id']['$oid'], new_user['email'], new_user['password']))
        except Exception as e:
            print(f"{type(e).__name__} {str(e)}")
            return FindUserResponse(500, f"{type(e).__name__} {str(e)}", "")

    def create_user(self, req: CreateUserRequest) -> CreateUserResponse:
        try:
            email = req.email
            password = req.password

            '''check if user exists'''
            user = self.collection.find_one({"email": f"{email}"})
            if not user:
                new_user = {
                    "email": f"{email}",
                    "password": f"{password}"
                }
                self.collection.insert_one(new_user)
                return CreateUserResponse(201, f"Successfully registered user")
            return CreateUserResponse(403, 'User already exists. Please login')
        except Exception as e:
            print(f"{type(e).__name__} {str(e)}")
            return CreateUserResponse(500, f"{type(e).__name__} {str(e)}")
