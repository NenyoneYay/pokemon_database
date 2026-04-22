import json
import random

with open('Database.json', 'r') as f:
    pokemonDict = json.load(f)
    pokemonList = pokemonDict["Pokemon"]




## MAIN ##

def main():
    iceList = filterType(pokemonList, "ice")
    bugList = filterType(pokemonList, "bug")
    fireList = filterType(pokemonList, "fire")
    rockList = filterType(pokemonList, "rock")
    darkList = filterType(pokemonList, "dark")
    grassList = filterType(pokemonList, "grass")
    fairyList = filterType(pokemonList, "fairy")    
    ghostList = filterType(pokemonList, "ghost")
    steelList = filterType(pokemonList, "steel") 
    waterList = filterType(pokemonList, "water")
    normalList = filterType(pokemonList, "normal")
    flyingList = filterType(pokemonList, "flying")
    poisonList = filterType(pokemonList, "poison")
    groundList = filterType(pokemonList, "ground")
    dragonList = filterType(pokemonList, "dragon")
    psychicList = filterType(pokemonList, "psychic")
    electricList = filterType(pokemonList, "electric")
    fightingList = filterType(pokemonList, "fighting") 
    generatePokemon(waterList)
    # generatePokemon(pokemonList)
    return

## DEFINE fUNCTIONS ##

def generatePokemon(list):
    limit = 0
    randHead = getRandomPokemon(list)
    while ((randHead["head"] != True)and(limit < 2000)):
        randHead = getRandomPokemon(list)
        limit += 1
    print (f"Head: {randHead["name"]}")
    limit = 0

    randBody = getRandomPokemon(list)
    while ((randBody["body"] != True)and(limit < 2000)):
        randBody = getRandomPokemon(list)
        limit += 1
    print (f"Body: {randBody["name"]}")
    limit = 0

    randEyes = getRandomPokemon(list)
    while ((randEyes["eyes"] != True)and(limit < 2000)):
        randEyes = getRandomPokemon(list)
        limit += 1
    print (f"Eyes: {randEyes["name"]}")
    limit = 0

    randMouth = getRandomPokemon(list)
    while ((randMouth["mouth"] != True)and(limit < 2000)):
        randMouth = getRandomPokemon(list)
        limit += 1
    print (f"Mouth: {randMouth["name"]}")
    limit = 0

    randFrontLeg = getRandomPokemon(list)
    while ((randFrontLeg["front_leg"] != True)and(limit < 2000)):
        randFrontLeg = getRandomPokemon(list)
        limit += 1
    print (f"Front Leg: {randFrontLeg["name"]}")
    limit = 0

    randBackLeg = getRandomPokemon(list)
    while ((randBackLeg["back_leg"] != True)and(limit < 2000)):
        randBackLeg = getRandomPokemon(list)
        limit += 1
    print (f"Back Leg: {randBackLeg["name"]}")
    limit = 0

    randTail = getRandomPokemon(list)
    while ((randTail["tail"] != True)and(limit < 2000)):
        randTail = getRandomPokemon(list)
        limit += 1
    print (f"Tail: {randTail["name"]}")
    limit = 0

    randEars = getRandomPokemon(list)
    while ((randEars["ears"] != True)and(2000)):
        randEars = getRandomPokemon(list)
        limit += 1
    print (f"Ears: {randEars["name"]}")
    limit = 0

    randHeadAccessory = getRandomPokemon(list)
    while ((randHeadAccessory["head_accessory"] != True)and(limit < 2000)):
        randHeadAccessory = getRandomPokemon(list)
        limit += 1
    print (f"Head Accessory: {randHeadAccessory["name"]}")
    limit = 0

    randNeckAccessory = getRandomPokemon(list)
    while ((randNeckAccessory["neck_accessory"] != True)and(limit < 2000)):
        randNeckAccessory = getRandomPokemon(list)
        limit += 1
    print (f"Neck Accessory: {randNeckAccessory["name"]}")
    limit = 0

    randLegAccessory = getRandomPokemon(list)
    while ((randLegAccessory["leg_accessory"] != True)and(limit < 2000)):
        randLegAccessory = getRandomPokemon(list)
        limit += 1
    print (f"Leg Accessory: {randLegAccessory["name"]}")
    limit = 0

    randDecoration = getRandomPokemon(list)
    while ((randDecoration["decoration"] != True)and(limit < 2000)):
        randDecoration = getRandomPokemon(list)
        limit += 1
    print (f"Decoration: {randDecoration["name"]}")
    limit = 0

    randColor = getRandomPokemon(list)
    print(f"Color scheme: {randColor["name"]}")

def filterType(list, type): ##Returns a list filtered by the type
    filteredList = []
    for pokemon in list:
        if ((pokemon["type1"] == type) or (pokemon["type2"] == type)):
            filteredList.append(pokemon)
    return filteredList

def getRandomPokemon(pokemonList): ## Takes a List of dicts as a parameter, returns a single dict randomly from that list
    dictLength = len(pokemonList) ## Get the length of the list of Pokemon
    return pokemonList[random.randrange(dictLength)] ## Return a Pokemon from the list randomly



if __name__ == '__main__':
    main()

