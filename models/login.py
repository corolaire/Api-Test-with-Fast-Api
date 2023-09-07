from pydantic import BaseModel,Field
from typing import Optional
class login(BaseModel):
    id:Optional[int]=None
    email:str=Field(min_length=10,max_length=30)
    password:str=Field(min_length=10,max_length=20)
    numberphone:int=Field(max_length=10)
    name:str=Field(min_length=4,max_length=15)