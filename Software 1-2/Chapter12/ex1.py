import requests

joke = requests.get("https://api.chucknorris.io/jokes/random")

print(joke.json()['value'])
