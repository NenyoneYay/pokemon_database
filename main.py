import json

with open('Database.json', 'r') as f:
    data = json.load(f)
    pokemonDict = json.loads(data)
# print(updatedData)
print(pokemonDict)




print("Hello world!")
