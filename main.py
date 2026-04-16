import json
import random


with open('Database.json', 'r') as f:
    pokemonDict = json.load(f)
    pokemonList = pokemonDict["Pokemon"]




def main():
    generatePokemon()
    return

def generatePokemon():
    randHead = getRandomPokemon(pokemonList)
    while (randHead["head"] != True):
        randHead = getRandomPokemon(pokemonList)
    print (f"Head: {randHead["name"]}")

    randBody = getRandomPokemon(pokemonList)
    while (randBody["body"] != True):
        randBody = getRandomPokemon(pokemonList)
    print (f"Body: {randBody["name"]}")

    randEyes = getRandomPokemon(pokemonList)
    while (randEyes["eyes"] != True):
        randEyes = getRandomPokemon(pokemonList)
    print (f"Eyes: {randEyes["name"]}")

    randMouth = getRandomPokemon(pokemonList)
    while (randMouth["mouth"] != True):
        randMouth = getRandomPokemon(pokemonList)
    print (f"Mouth: {randMouth["name"]}")

    randFrontLeg = getRandomPokemon(pokemonList)
    while (randFrontLeg["front_leg"] != True):
        randFrontLeg = getRandomPokemon(pokemonList)
    print (f"FrontLeg: {randFrontLeg["name"]}")

    randBackLeg = getRandomPokemon(pokemonList)
    while (randBackLeg["back_leg"] != True):
        randBackLeg = getRandomPokemon(pokemonList)
    print (f"BackLeg: {randBackLeg["name"]}")

    randTail = getRandomPokemon(pokemonList)
    while (randTail["tail"] != True):
        randTail = getRandomPokemon(pokemonList)
    print (f"Tail: {randTail["name"]}")

    randEars = getRandomPokemon(pokemonList)
    while (randEars["ears"] != True):
        randEars = getRandomPokemon(pokemonList)
    print (f"Ears: {randEars["name"]}")

    randHeadAccessory = getRandomPokemon(pokemonList)
    while (randHeadAccessory["head_accessory"] != True):
        randHeadAccessory = getRandomPokemon(pokemonList)
    print (f"HeadAccessory: {randHeadAccessory["name"]}")

    randNeckAccessory = getRandomPokemon(pokemonList)
    while (randNeckAccessory["neck_accessory"] != True):
        randNeckAccessory = getRandomPokemon(pokemonList)
    print (f"NeckAccessory: {randNeckAccessory["name"]}")

    randLegAccessory = getRandomPokemon(pokemonList)
    while (randLegAccessory["leg_accessory"] != True):
        randLegAccessory = getRandomPokemon(pokemonList)
    print (f"LegAccessory: {randLegAccessory["name"]}")

    randDecoration = getRandomPokemon(pokemonList)
    while (randDecoration["decoration"] != True):
        randDecoration = getRandomPokemon(pokemonList)
    print (f"Decoration: {randDecoration["name"]}")


def getRandomPokemon(pokemonList): ## Takes a List of dicts as a parameter, returns a single dict randomly from that list
    dictLength = len(pokemonList) ## Get the length of the list of Pokemon
    return pokemonList[random.randrange(dictLength)] ## Return a Pokemon from the list randomly








if __name__ == '__main__':
    main()

