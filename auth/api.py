from fastapi import APIRouter, Response, status
from starlette.requests import Request

# from starlette.templating import Jinja2Templates
from .validators import UserValidator
#from . import schemas, models

# templates = Jinja2Templates(directory="templates")

user_router = APIRouter(prefix="/users", tags=["auth"])


@user_router.get("/")
async def index(request: Request):
    return "hi from user api Router"
    # return templates.TemplateResponse("auth.html", {"request": request})


# @user_router.post("/registartion", tags=["auth"])
# async def create_user(user: models.User, response: Response):
#     print(UserValidator(user))
#     print(user)
#     if not UserValidator(user):
#         response.status_code = status.HTTP_400_BAD_REQUEST
#     elif False:  # проверка email по базе
#         response.status_code = status.HTTP_409_CONFLICT
#     elif False:  # проверка на авторизированного ползователя
#         response.status_code = status.HTTP_403_FORBIDDEN
#     else:
#         return await user.save()
#         # print(user)
#         # user_db = await models.User.objects.fields(['id','firstNmae', 'lastName','email']).get(id=user.id)#get(id = user.id)#exclude_fields(['password']).get(id = user.id)

#         # return user_db
#     return "unknown error"
