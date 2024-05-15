import requests


URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '9514938c409c7c6bcf7b551a5426bf69'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
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


'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print (response.text)'''

"""response_confirmation = requests.post(url=f'{URL}/trainers/confirm_email', headers= HEADER, json= body_confirmation)
print (response_confirmation.text)"""


response_create = requests.post(url=f'{URL}/pokemons', headers= HEADER, json= body_create)
print(response_create.text)

pokemon_ID = response_create.json()['id']
print(pokemon_ID)