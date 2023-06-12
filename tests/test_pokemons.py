import requests
import pytest

host = 'https://pokemonbattle.me:9104'

def test_status_code():
     answer = requests.get(f'{host}/trainers')

     assert answer.status_code == 200

def test_trainer_id():
     id= requests.get(f'{host}/trainers', params = {'trainer_id': 4672})
     
     assert id.json()['trainer_name']=='MAX'
