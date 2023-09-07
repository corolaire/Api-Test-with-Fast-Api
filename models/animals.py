from pydantic import BaseModel,Field
from typing import Optional
class animals(BaseModel):
    id:Optional[int]=None
    age:int=Field(min_length=1,max_length=3)
    hair_color:str=Field(min_length=1)
    eyes_color:str=Field(min_length=1)
    weight:float=Field(min_length=1,gt=0)
    character:str=Field(min_length=1, max_length=100)
    size:str=Field(min_length=1,max_length=50)
    diseases:str=Field(min_length=50 , max_length=300)
    disabilities:str=Field(min_length=50,max_length=300)
#pasa el modelo en fastapi como si fuese una request en flask , el formato es igual y usa pydantic para validar .
#aca le llama esquema.