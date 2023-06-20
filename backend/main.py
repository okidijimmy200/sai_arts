import os
from pymongo import MongoClient
from server.http.server import get_app
from storage.mongo import MongoStorage as Mongo
from service.user.users import Registration
from service.auth.auth import Authentication


if __name__ == '__main__':
    mongo_db = MongoClient(os.environ['DATABASE_LOCAL'])
    database = os.environ['Database']
    collection = os.environ['Collection']
    
    app = get_app(
        Registration(Mongo(mongo_db, database, collection)),
        Authentication(Mongo(mongo_db, database, collection))
    )
    app.run(host='localhost', port=8000, debug=True)