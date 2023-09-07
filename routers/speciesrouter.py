from fastapi import APIRouter,Query,Path
from models import species
router=APIRouter()

@router.get('/species/{name}')
def get_species_name(name:str):
     return list(filter(lambda item:item['name']==name,species))
 

