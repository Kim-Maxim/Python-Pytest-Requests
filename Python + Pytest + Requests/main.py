import requests

token = '688c65a88879360ef8ea8335939216fa'

answer = requests.post('https://pokemonbattle.me:9104/trainers/reg', json=
  {
    "trainer_token": token,
    "email": "maxim@dolnikov.ru",
    "password": "Iloveqa1"
}, headers = {"Content-Type": "application/json"}                    )

host = 'https://pokemonbattle.me:9104'

answer_confirm = requests.post(f'{host}//trainers/confirm_email', json = 
                               {
    "trainer_token": token
}, headers = {"Content-Type": "application/json"})

create_pokemon = requests.post(f'{host}/pokemons', json = 
                               {
    "name": "Бульба666",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
        
}, headers = {"Content-Type": "application/json", "trainer_token": token })      

print(create_pokemon.text)

change_name = requests.put(f'{host}/pokemons', json = 
                           {
    "pokemon_id": "13087",
    "name": "Бульба777",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers = {"Content-Type": "application/json", "trainer_token": token })

print(change_name.text)

add_pokeball = requests.post(f'{host}/trainers/add_pokeball', json = 
                             {
    "pokemon_id": "13087"
}, headers = {"Content-Type": "application/json", "trainer_token": token })

print(add_pokeball.json)
                             
