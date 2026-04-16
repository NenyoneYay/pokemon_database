import json
import random


with open('Database.json', 'r') as f:
    pokemonDict = json.load(f)
    pokemonList = pokemonDict["Pokemon"]




def main():
    generatePokemon(pokemonList)
    return

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


def getRandomPokemon(pokemonList): ## Takes a List of dicts as a parameter, returns a single dict randomly from that list
    dictLength = len(pokemonList) ## Get the length of the list of Pokemon
    return pokemonList[random.randrange(dictLength)] ## Return a Pokemon from the list randomly








if __name__ == '__main__':
    main()

