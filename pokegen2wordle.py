guess = ''
#will promptimport random

# Dictionary of Generation 2 Pokémon with their colors and types
pokemon_data = {
    "chikorita": {"color": "green", "type": "grass", "secondary_color": "", "secondary_type": ""},
    "bayleef": {"color": "green", "type": "grass", "secondary_color": "", "secondary_type": ""},
    "meganium": {"color": "green", "type": "grass", "secondary_color": "", "secondary_type": ""},
    "cyndaquil": {"color": "brown", "type": "fire", "secondary_color": "", "secondary_type": ""},
    "quilava": {"color": "brown", "type": "fire", "secondary_color": "", "secondary_type": ""},
    "typhlosion": {"color": "brown", "type": "fire", "secondary_color": "", "secondary_type": ""},
    "totodile": {"color": "blue", "type": "water", "secondary_color": "", "secondary_type": ""},
    "croconaw": {"color": "blue", "type": "water", "secondary_color": "", "secondary_type": ""},
    "feraligatr": {"color": "blue", "type": "water", "secondary_color": "", "secondary_type": ""},
    "sentret": {"color": "brown", "type": "normal", "secondary_color": "", "secondary_type": ""},
    "furret": {"color": "brown", "type": "normal", "secondary_color": "", "secondary_type": ""},
    "hoothoot": {"color": "brown", "type": "normal", "secondary_color": "white", "secondary_type": "flying"},
    "noctowl": {"color": "brown", "type": "normal", "secondary_color": "white", "secondary_type": "flying"},
    "ledyba": {"color": "red", "type": "bug", "secondary_color": "", "secondary_type": "flying"},
    "ledian": {"color": "red", "type": "bug", "secondary_color": "", "secondary_type": "flying"},
    "spinarak": {"color": "green", "type": "bug", "secondary_color": "yellow", "secondary_type": "poison"},
    "ariados": {"color": "red", "type": "bug", "secondary_color": "yellow", "secondary_type": "poison"},
    "crobat": {"color": "purple", "type": "poison", "secondary_color": "black", "secondary_type": "flying"},
    "chinchou": {"color": "blue", "type": "water", "secondary_color": "yellow", "secondary_type": "electric"},
    "lanturn": {"color": "blue", "type": "water", "secondary_color": "yellow", "secondary_type": "electric"},
    "pichu": {"color": "yellow", "type": "electric", "secondary_color": "", "secondary_type": ""},
    "cleffa": {"color": "pink", "type": "fairy", "secondary_color": "", "secondary_type": ""},
    "igglybuff": {"color": "pink", "type": "normal", "secondary_color": "", "secondary_type": "fairy"},
    "togepi": {"color": "white", "type": "fairy", "secondary_color": "", "secondary_type": ""},
    "togetic": {"color": "blue", "type": "fairy", "secondary_color": "white", "secondary_type": "flying"},
    "natu": {"color": "green", "type": "psychic", "secondary_color": "blue", "secondary_type": "flying"},
    "xatu": {"color": "green", "type": "psychic", "secondary_color": "blue", "secondary_type": "flying"},
    "mareep": {"color": "yellow", "type": "electric", "secondary_color": "", "secondary_type": ""},
    "flaaffy": {"color": "pink", "type": "electric", "secondary_color": "", "secondary_type": ""},
    "ampharos": {"color": "yellow", "type": "electric", "secondary_color": "", "secondary_type": ""},
    "bellossom": {"color": "green", "type": "grass", "secondary_color": "", "secondary_type": ""},
    "marill": {"color": "blue", "type": "water", "secondary_color": "", "secondary_type": "fairy"},
    "azumarill": {"color": "blue", "type": "water", "secondary_color": "", "secondary_type": "fairy"},
    "sudowoodo": {"color": "brown", "type": "rock", "secondary_color": "", "secondary_type": ""},
    "politoed": {"color": "green", "type": "water", "secondary_color": "", "secondary_type": ""},
    "hoppip": {"color": "pink", "type": "grass", "secondary_color": "green", "secondary_type": "flying"},
    "skiploom": {"color": "green", "type": "grass", "secondary_color": "pink", "secondary_type": "flying"},
    "jumpluff": {"color": "blue", "type": "grass", "secondary_color": "pink", "secondary_type": "flying"},
    "aipom": {"color": "purple", "type": "normal", "secondary_color": "", "secondary_type": ""},
    "sunkern": {"color": "yellow", "type": "grass", "secondary_color": "", "secondary_type": ""},
    "sunflora": {"color": "yellow", "type": "grass", "secondary_color": "", "secondary_type": ""},
    "yanma": {"color": "red", "type": "bug", "secondary_color": "green", "secondary_type": "flying"},
    "wooper": {"color": "blue", "type": "water", "secondary_color": "pink", "secondary_type": "ground"},
    "quagsire": {"color": "blue", "type": "water", "secondary_color": "pink", "secondary_type": "ground"},
    "espeon": {"color": "purple", "type": "psychic", "secondary_color": "", "secondary_type": ""},
    "umbreon": {"color": "black", "type": "dark", "secondary_color": "", "secondary_type": ""},
    "murkrow": {"color": "black", "type": "dark", "secondary_color": "yellow", "secondary_type": "flying"},
    "slowking": {"color": "pink", "type": "water", "secondary_color": "", "secondary_type": "psychic"},
    "misdreavus": {"color": "black", "type": "ghost", "secondary_color": "", "secondary_type": ""},"misdreavus": {"color": "black", "type": "ghost"},
    "unown": {"color": "black", "type": "psychic", "secondary_color": "", "secondary_type": ""},
    "wobbuffet": {"color": "blue", "type": "psychic", "secondary_color": "", "secondary_type": ""},
    "girafarig": {"color": "yellow", "type": "normal", "secondary_color": "", "secondary_type": "psychic"},
    "pineco": {"color": "gray", "type": "bug", "secondary_color": "", "secondary_type": ""},
    "forretress": {"color": "purple", "type": "bug", "secondary_color": "", "secondary_type": "steel"},
    "dunsparce": {"color": "yellow", "type": "normal", "secondary_color": "", "secondary_type": ""},
    "gligar": {"color": "purple", "type": "ground", "secondary_color": "blue", "secondary_type": "flying"},
    "steelix": {"color": "gray", "type": "steel", "secondary_color": "", "secondary_type": "ground"},
    "snubbull": {"color": "pink", "type": "fairy", "secondary_color": "", "secondary_type": ""},
    "granbull": {"color": "purple", "type": "fairy", "secondary_color": "", "secondary_type": ""},
    "qwilfish": {"color": "gray", "type": "water", "secondary_color": "", "secondary_type": "poison"},
    "scizor": {"color": "red", "type": "bug", "secondary_color": "gray", "secondary_type": "steel"},
    "shuckle": {"color": "yellow", "type": "bug", "secondary_color": "red", "secondary_type": "rock"},
    "heracross": {"color": "blue", "type": "bug", "secondary_color": "red", "secondary_type": "fighting"},
    "sneasel": {"color": "black", "type": "dark", "secondary_color": "red", "secondary_type": "ice"},
    "teddiursa": {"color": "black", "type": "normal", "secondary_color": "", "secondary_type": ""},
    "ursaring": {"color": "brown", "type": "normal", "secondary_color": "", "secondary_type": ""},
    "slugma": {"color": "red", "type": "fire", "secondary_color": "", "secondary_type": ""},
    "magcargo": {"color": "red", "type": "fire", "secondary_color": "gray", "secondary_type": "rock"},
    "swinub": {"color": "brown", "type": "ice", "secondary_color": "pink", "secondary_type": "ground"},
    "piloswine": {"color": "brown", "type": "ice", "secondary_color": "pink", "secondary_type": "ground"},
    "corsola": {"color": "pink", "type": "water", "secondary_color": "blue", "secondary_type": "rock"},
    "remoraid": {"color": "blue", "type": "water", "secondary_color": "", "secondary_type": ""},
    "octillery": {"color": "red", "type": "water", "secondary_color": "", "secondary_type": ""},
    "delibird": {"color": "red", "type": "ice", "secondary_color": "white", "secondary_type": "flying"},
    "mantine": {"color": "purple", "type": "water", "secondary_color": "blue", "secondary_type": "flying"},
    "skarmory": {"color": "gray", "type": "steel", "secondary_color": "red", "secondary_type": "flying"},
    "houndour": {"color": "black", "type": "dark", "secondary_color": "red", "secondary_type": "fire"},
    "houndoom": {"color": "black", "type": "dark", "secondary_color": "red", "secondary_type": "fire"},
    "kingdra": {"color": "blue", "type": "water", "secondary_color": "purple", "secondary_type": "dragon"},
    "phanpy": {"color": "blue", "type": "ground", "secondary_color": "", "secondary_type": ""},
    "donphan": {"color": "gray", "type": "ground", "secondary_color": "", "secondary_type": ""},
    "porygon2": {"color": "red", "type": "normal", "secondary_color": "", "secondary_type": ""},
    "stantler": {"color": "brown", "type": "normal", "secondary_color": "", "secondary_type": ""},
    "smeargle": {"color": "white", "type": "normal", "secondary_color": "", "secondary_type": ""},"smeargle": {"color": "white", "type": "normal"},
    "hitmontop": {"color": "brown", "type": "fighting", "secondary_color": "", "secondary_type": ""},
    "smoochum": {"color": "pink", "type": "ice", "secondary_color": "", "secondary_type": "psychic"},
    "elekid": {"color": "yellow", "type": "electric", "secondary_color": "", "secondary_type": ""},
    "magby": {"color": "red", "type": "fire", "secondary_color": "", "secondary_type": ""},
    "miltank": {"color": "pink", "type": "normal", "secondary_color": "", "secondary_type": ""},
    "blissey": {"color": "pink", "type": "normal", "secondary_color": "", "secondary_type": ""},
    "raikou": {"color": "yellow", "type": "electric", "secondary_color": "", "secondary_type": ""},
    "entei": {"color": "brown", "type": "fire", "secondary_color": "", "secondary_type": ""},
    "suicune": {"color": "blue", "type": "water", "secondary_color": "", "secondary_type": ""},
    "larvitar": {"color": "green", "type": "rock", "secondary_color": "brown", "secondary_type": "ground"},
    "pupitar": {"color": "gray", "type": "rock", "secondary_color": "brown", "secondary_type": "ground"},
    "tyranitar": {"color": "green", "type": "rock", "secondary_color": "black", "secondary_type": "dark"},
    "lugia": {"color": "white", "type": "psychic", "secondary_color": "blue", "secondary_type": "flying"},
    "ho-oh": {"color": "red", "type": "fire", "secondary_color": "yellow", "secondary_type": "flying"},
    "celebi": {"color": "green", "type": "psychic", "secondary_color": "", "secondary_type": "grass"},
    #list of every gen2 pokemon with their types and colors
}
random_pokemon = random.choice(list(pokemon_data.keys()))
print("Random Pokémon:", random_pokemon)

def select_pokemon():
    return random_pokemon
def check_guess(pokemon, guess):
    guess = guess.lower()
    if guess == pokemon:
        return "You guessed it! Congratulations!"
    elif len(guess) != len(pokemon):
        return "WRONG!"
   
def hint(guess, pokemon):
    # Check if the guessed Pokémon exists in the dictionary
    if guess not in pokemon_data:
        print("Invalid Pokémon. Please guess a valid Generation 2 Pokémon.")
        return

    # Get the data of the guessed Pokémon
    guess_data = pokemon_data[guess]

    # Check if the guessed Pokémon matches the randomly selected Pokémon
    if guess == pokemon:
        print("Congratulations! You've guessed the Pokémon correctly:", pokemon)
        return

    # Check if the color matches
    if guess_data["color"] == pokemon_data[pokemon]["color"]:
        print("The color of the Pokémon matches.")

    # Check if the type matches
    if guess_data["type"] == pokemon_data[pokemon]["type"]:
        print("The type of the Pokémon matches.")

    # Check if the secondary color matches
    if guess_data["secondary_color"] == pokemon_data[pokemon]["secondary_color"]:
        print("The secondary color of the Pokémon matches.")

    # Check if the secondary type matches
    if guess_data["secondary_type"] == pokemon_data[pokemon]["secondary_type"]:
        print("The secondary type of the Pokémon matches.")


def play_wordle():
    pokemon = select_pokemon()
    print("Welcome to Pokémon Wordle!")
    print("Try to guess the name of a Generation 2 Pokémon.")
    print("You have 6 attempts. Good luck!")
    print("")

    attempts = 0
    while attempts < 6:
        guess = input("Enter your guess: ")
        result = check_guess(pokemon, guess)
        print(result)
        print("")
        if result != "You guessed it! Congratulations!":
            print(hint(pokemon, guess))
        attempts += 1
        if result == "You guessed it! Congratulations!":
            break
    if attempts == 6:
        print(f"Sorry, you didn't guess the Pokémon. It was {pokemon.capitalize()}.")

if __name__ == "__main__":
    play_wordle()
 the user to guess a word
lives = 8
#the ammount of tries given to the player
pokemon = ("Chikorita", "Bayleef", "Meganium", "Cyndaquil", "Quilava", "Typhlosion", "Totodile", "Croconaw", "Feraligatr", "Sentret", "Furret", "Hoothoot", "Noctowl", "Ledyba", "Ledian", "Spinarak", "Ariados", "Crobat", "Chinchou", "Lanturn", "Pichu", "Cleffa", "Igglybuff", "Togepi", "Togetic", "Natu", "Xatu", "Mareep", "Flaaffy", "Ampharos", "Bellossom", "Marill", "Azumarill", "Sudowoodo", "Politoed", "Hoppip", "Skiploom", "Jumpluff", "Aipom", "Sunkern", "Sunflora", "Yanma", "Wooper", "Quagsire", "Espeon", "Umbreon", "Murkrow", "Slowking", "Misdreavus", "Unown", "Wobbuffet", "Girafarig", "Pineco", "Forretress", "Dunsparce", "Gligar", "Steelix", "Snubbull", "Granbull", "Qwilfish", "Scizor", "Shuckle", "Heracross", "Sneasel", "Teddiursa", "Ursaring", "Slugma", "Magcargo", "Swinub", "Piloswine", "Corsola", "Remoraid", "Octillery", "Delibird", "Mantine", "Skarmory", "Houndour", "Houndoom", "Kingdra", "Phanpy", "Donphan", "Porygon2", "Stantler", "Smeargle", "Tyrogue", "Hitmontop", "Smoochum", "Elekid", "Magby", "Miltank", "Blissey", "Raikou", "Entei", "Suicune", "Larvitar", "Pupitar", "Tyranitar", "Lugia", "Ho-Oh", "Celebi")
#list of Pokemon
rPokemon = ["Chikorita", "Bayleef", "Meganium", "Cyndaquil", "Quilava", "Typhlosion", "Totodile", "Croconaw", "Feraligatr", "Sentret", "Furret", "Hoothoot", "Noctowl", "Ledyba", "Ledian", "Spinarak", "Ariados", "Crobat", "Chinchou", "Lanturn", "Pichu", "Cleffa", "Igglybuff", "Togepi", "Togetic", "Natu", "Xatu", "Mareep", "Flaaffy", "Ampharos", "Bellossom", "Marill", "Azumarill", "Sudowoodo", "Politoed", "Hoppip", "Skiploom", "Jumpluff", "Aipom", "Sunkern", "Sunflora", "Yanma", "Wooper", "Quagsire", "Espeon", "Umbreon", "Murkrow", "Slowking", "Misdreavus", "Unown", "Wobbuffet", "Girafarig", "Pineco", "Forretress", "Dunsparce", "Gligar", "Steelix", "Snubbull", "Granbull", "Qwilfish", "Scizor", "Shuckle", "Heracross", "Sneasel", "Teddiursa", "Ursaring", "Slugma", "Magcargo", "Swinub", "Piloswine", "Corsola", "Remoraid", "Octillery", "Delibird", "Mantine", "Skarmory", "Houndour", "Houndoom", "Kingdra", "Phanpy", "Donphan", "Porygon2", "Stantler", "Smeargle", "Tyrogue", "Hitmontop", "Smoochum", "Elekid", "Magby", "Miltank", "Blissey", "Raikou", "Entei", "Suicune", "Larvitar", "Pupitar", "Tyranitar", "Lugia", "Ho-Oh", "Celebi"]
#list meant for program to choose a random Pokemon
import random

randomp = (random.choice(rPokemon))
print (randomp)
#function chooses a random pokemon from rPokemon
loop = True
while loop:
    print("Start the Game? (yes/no)")
    command = input()
    if command == "no":
            loop = False
    elif command == "yes":
            inner_loop = 0
    while guess != (randomp):
        guess = input("Guess a Word: ")
    if guess == (randomp):
        print("CORRECT!")
    else:
        lives = (lives - 1)
        print("ATTEMPTS REMAINING: "+str(lives))
        print("INCORRECT!")
        if lives == 1:
            break
    

    




         



    
