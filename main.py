import json

with open('Database.json', 'r') as f:
    data = json.load(f)

print(json.dumps(data, indent = 4))



print("Hello world!")
