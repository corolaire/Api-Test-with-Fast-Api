from fastapi import FastAPI 

app=FastAPI()  # create app
animals=[{
    'id':'1',
    'age':20,
    'hair_color':'brown',
    'eyes_color':'blue',
    'weight':15,
    'character':'good',
    
    
},
{
      'id':'2',
      'age':3,
      'hair_color':'blondie',
      'eyes_color':'brown',
      'weight':10,
      'character':'calm '      
}     
  ]
@app.get('/')
def message():
    return 'Welcome to my page  '

@app.get('/animals')
def add_animals():
    return animals 
    
@app.get('/animals/{id}')
def get_animals(id:str):
    return list(filter(lambda item:item['id']==id,animals))
    
#parametros query:yo quiero acceder a una caracteristica determinada detro de animales.
@app.get('/animals/{age}')
def get_animals_by_age (age:int):#le paso el parametro
    return list(filter (lambda item:item['age']==age,animals))#filtra x edad y compara si la edad entrante es igual a la q tenes
        
@app.get('/animals/{hair_color}')
def get_animal_by_hair_color(hair_color:str):
    return list(filter(lambda item:item['hair_color']==hair_color,animals))  
@app.get('/animals/{eyes_color}')
def get_animals_by_eyes_color(eyes_color:str):
    return list(filter(lambda item:item['eyes_color']==eyes_color,animals))

@app.get('/animals/{character}')
def get_animals_by_character(character:str):
    return list(filter(lambda item:item['character']==character,animals))

@app.get('/animals/{weight}')
def get_animals_by_weight(weight:int):
    return list(filter(lambda item:item['weight']==weight,animals)) 










if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,port=8000)

