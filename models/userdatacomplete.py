from pydantic import BaseModel,Field
from typing import Optional
class userdatacomplete(BaseModel):
    id:Optional[int]=None
    name:str=Field(min_length=3,max_length=15)
    lastname:str=Field(min_length=2,max_length=20)
    numberphone:int=Field(min_length=10,max_length=10)
    email:str=Field(min_length=3,max_length=320)
    otherphone:int=Field(min_length=8,max_length=15)
    age:int=Field(min_length=2,max_length=2, ge=18,le=100)
    where_live:str=Field(min_length= 4   ,max_length=50)
    