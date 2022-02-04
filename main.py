from fastapi import FastAPI

api = FastAPI()

@api.get('/')
def index():
  return {'message': 'Petit test de fastapi',
          'status': 'Retour sur ce petit success'}
  
@api.get('/list')
def list():
  return [{'id': 1, 'description': 'description 1'},
          {'id': 2, 'description': 'description 2'},
          {'id': 3, 'description': 'description 3'},
          {'id': 4, 'description': 'description 4'},
          {'id': 5, 'description': 'description 5'}
          ]