from fastapi import APIRouter,Path,Query
from models import login

router=APIRouter()


@router.get('/login/{email}')
def get_login_email(email:str):
    return list(filter (lambda item:item['email']==email,login))

@router.get('/login/{password}')
def get_password(password:str):
    return list(filter(lambda item:item['password']==password,login))

@router.get('/login/{numberphone}')
def get_login_numberphone(numberphone:int):
    return list(filter(lambda item:item['numberphone']==numberphone,login))

@router.get('/login/{name}')
def get_login_name(name:str):
    return list(filter(lambda item:item[name]==name,login))


