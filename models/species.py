from pydantic import BaseModel,Field
from typing import Optional

class species(BaseModel):
    id:Optional[int]=None
    name:str=Field(min_length=3,max_length=20)