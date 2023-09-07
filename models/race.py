from pydantic import BaseModel,Field
from typing import Optional
class race ( BaseModel):
    id:Optional[int]=None
    name:str=Field(min_length=1,max_length=15)
