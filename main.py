import requests


URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '9514938c409c7c6bcf7b551a5426bf69'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}

body_create = {
    "name": "Kadavr2",
    "photo": "https://dolnikov.ru/pokemons/albums/048.png"
}



response_create = requests.post(url=f'{URL}/pokemons', headers= HEADER, json= body_create)
print(response_create.text)

pokemon_ID = response_create.json()['id']
print('Айди покемона:', pokemon_ID)

body_edit = {
    "pokemon_id": pokemon_ID,
    "name": "New Kadavr",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body_to_pokeball = {
    "pokemon_id": pokemon_ID
}
    
response_edit_pokemon = requests.put (url=f'{URL}/pokemons', headers=HEADER, json=body_edit)
print(response_edit_pokemon.text)

response_to_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers= HEADER, json= body_to_pokeball)
print(response_to_pokeball.text)

