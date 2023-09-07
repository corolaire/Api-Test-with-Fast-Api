from fastapi import APIRouter,Path,Query
from models import race
router=APIRouter()

@router.get('/race/{name}')  
def get_race_name(name:str):
     return list(filter(lambda item:item['name']==name,race))
 
 