import json
import random

with open('Database.json', 'r') as f:
    pokemonDict = json.load(f)
    pokemonList = pokemonDict["Pokemon"]




## MAIN ##

def main():
    grassList = filterType(pokemonList, "grass")
    fireList = filterType(pokemonList, "fire")
    waterList = filterType(pokemonList, "water")
    electricList = filterType(pokemonList, "electric")
    psychicList = filterType(pokemonList, "psychic")
    iceList = filterType(pokemonList, "ice")
    dragonList = filterType(pokemonList, "dragon")
    darkList = filterType(pokemonList, "dark")
    fairyList = filterType(pokemonList, "fairy")
    normalList = filterType(pokemonList, "normal")
    fightingList = filterType(pokemonList, "fighting")
    flyingList = filterType(pokemonList, "flying")
    poisonList = filterType(pokemonList, "poison")
    groundList = filterType(pokemonList, "ground")
    rockList = filterType(pokemonList, "rock")
    bugList = filterType(pokemonList, "bug")
    ghostList = filterType(pokemonList, "ghost")
    steelList = filterType(pokemonList, "steel")
    generatePokemon(pokemonList)
    # generatePokemon(pokemonList)
    return

## DEFINE fUNCTIONS ##

def generatePokemon(list):
    randHead = getRandomPokemon(list)
    while (randHead["head"] != True):
        randHead = getRandomPokemon(list)
    print (f"Head: {randHead["name"]}")

    randBody = getRandomPokemon(list)
    while (randBody["body"] != True):
        randBody = getRandomPokemon(list)
    print (f"Body: {randBody["name"]}")

    randEyes = getRandomPokemon(list)
    while (randEyes["eyes"] != True):
        randEyes = getRandomPokemon(list)
    print (f"Eyes: {randEyes["name"]}")

    randMouth = getRandomPokemon(list)
    while (randMouth["mouth"] != True):
        randMouth = getRandomPokemon(list)
    print (f"Mouth: {randMouth["name"]}")

    randFrontLeg = getRandomPokemon(list)
    while (randFrontLeg["front_leg"] != True):
        randFrontLeg = getRandomPokemon(list)
    print (f"FrontLeg: {randFrontLeg["name"]}")

    randBackLeg = getRandomPokemon(list)
    while (randBackLeg["back_leg"] != True):
        randBackLeg = getRandomPokemon(list)
    print (f"BackLeg: {randBackLeg["name"]}")

    randTail = getRandomPokemon(list)
    while (randTail["tail"] != True):
        randTail = getRandomPokemon(list)
    print (f"Tail: {randTail["name"]}")

    randEars = getRandomPokemon(list)
    while (randEars["ears"] != True):
        randEars = getRandomPokemon(list)
    print (f"Ears: {randEars["name"]}")

    randHeadAccessory = getRandomPokemon(list)
    while (randHeadAccessory["head_accessory"] != True):
        randHeadAccessory = getRandomPokemon(list)
    print (f"HeadAccessory: {randHeadAccessory["name"]}")

    randNeckAccessory = getRandomPokemon(list)
    while (randNeckAccessory["neck_accessory"] != True):
        randNeckAccessory = getRandomPokemon(list)
    print (f"NeckAccessory: {randNeckAccessory["name"]}")

    randLegAccessory = getRandomPokemon(list)
    while (randLegAccessory["leg_accessory"] != True):
        randLegAccessory = getRandomPokemon(list)
    print (f"LegAccessory: {randLegAccessory["name"]}")

    randDecoration = getRandomPokemon(list)
    while (randDecoration["decoration"] != True):
        randDecoration = getRandomPokemon(list)
    print (f"Decoration: {randDecoration["name"]}")

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

