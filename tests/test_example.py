import requests
import pytest


URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '9514938c409c7c6bcf7b551a5426bf69'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = 4088

body_registration = {
    "trainer_token": TOKEN,
    "email": "ferdal@mail.ru",
    "password": "Odin123"
}
body_confirmation = {
    "trainer_token" : TOKEN
}
body_create = {
    "name": "Kadavr",
    "photo": "https://dolnikov.ru/pokemons/albums/048.png"
}


def test_status_code():
    response = requests.get(url=f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_pokemon_lvl():
     response_lvl = requests.get(url=f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
     assert response_lvl.json()['data'][2]['stage'] == '1'

@pytest.mark.parametrize('key, value', [('name', 'Kadavr'),('trainer_id',f'{TRAINER_ID}'),('id', '27298'),('stage', '1')])
def test_param(key, value):
    response_param = requests.get(url=f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    assert response_param.json()["data"][0][key] == value