from fastapi import APIRouter,Path,Query
from models import animals 

router=APIRouter()


@router.get('/animals')
def add_animals():
    return animals 
    
@router.get('/animals/{id}')
def get_animals(id:str):
    return list(filter(lambda item:item['id']==id,animals))
#parametros query:yo quiero acceder a una caracteristica determinada detro de animales.
@router.get('/animals/{age}')
def get_animals_by_age (age:int):#le paso el parametro
    return list(filter (lambda item:item['age']==age,animals))#filtra x edad y compara si la edad entrante es igual a la q tenes
        
@router.get('/animals/{hair_color}')
def get_animal_by_hair_color(hair_color:str):
    return list(filter(lambda item:item['hair_color']==hair_color,animals))  
@router.get('/animals/{eyes_color}')
def get_animals_by_eyes_color(eyes_color:str):
    return list(filter(lambda item:item['eyes_color']==eyes_color,animals))

@router.get('/animals/{character}')
def get_animals_by_character(character:str):
    return list(filter(lambda item:item['character']==character,animals))

@router.get('/animals/{weight}')
def get_animals_by_weight(weight:float):
    return list(filter(lambda item:item['weight']==weight,animals)) 

@router.get('/animals/{disabilities}')
def get_animal_disabilities(disabilities:str):
    return list(filter(lambda item:item['disabilities']==disabilities,animals))

@router.get('/animals/{size}')
def get_animal_size(size:str):
    return list(filter(lambda item:item['size']==size,animals))

@router.get('/animals/{diseases}')
def get_animal_diseases(diseases:str):
    return list(filter(lambda item:item['diseases']==diseases,animals))