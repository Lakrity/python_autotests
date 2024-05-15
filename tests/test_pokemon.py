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
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    assert response.status_code == 200

@pytest.mark.parametrize('key, value', [('trainer_name', 'Shpunsel'),('id',f'{TRAINER_ID}'),
                                        ('city', 'Enakievo'),('is_premium', False)])
def test_param(key, value):
    response_param = requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    assert response_param.json()["data"][0][key] == value