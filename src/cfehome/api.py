from ninja import NinjaAPI, Schema

from ninja_extra import NinjaExtraAPI
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.controller import NinjaJWTDefaultController

api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)

class UserSchema(Schema):
    username: str
    is_authenticated: bool
    # in not request.use.is_authenticated 
    email: str = None

class MemberSchema(Schema):
    name: str 
    phone: int
    status: bool


@api.get("/hello")
def hello(request):
    print(request)
    return "Hello World"

@api.get("/himel")
def himel(request):
    print(request)
    return "himel"

@api.get('/me', response=UserSchema, auth=JWTAuth())
def me(request):
    print(request)
    return request.user

@api.get('/member', response=MemberSchema)
def member(request):
    print(request)
    return {
        "name": "John Doe",
        "phone": 1234567890,
        "status": True
    }

 