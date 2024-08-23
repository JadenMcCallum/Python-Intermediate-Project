import requests




ask = input("Which pokemon would you like to pick? ")
ask = ask.lower() 

url = requests.get(f"https://pokeapi.co/api/v2/pokemon/{ask}")
person = url.json()

print(f"This is: {person["name"]}")
print(f"Their height is: {person["height"]}")
print(f"They're in order: {person["order"]}")
print(f"Their weight is: {person["weight"]}")
print(f"Their experience is: {person["base_experience"]}")
