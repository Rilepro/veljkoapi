
from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT


from security import authenticate, identity
from resource.user import UserRegister
from resource.item import Item, ItemList

app= Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity) #/auth

# komentar za git
# drugi komentar za git

api.add_resource(Item, '/item/<string:name>')  #http://127.0.0.1:5000/item/chair
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)

    app.run(port=5000, debug=True)





