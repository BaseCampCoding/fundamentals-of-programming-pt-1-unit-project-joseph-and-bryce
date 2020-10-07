import random
import simple_colors
from simple_colors import *
import art
from art import *
mad_libs = text2art("Mad Libs")
print(mad_libs)      

print("Hello user elcome to Bryce and Joseph's custom Mad Lib!")
input("Press Enter to start")
nouns = ("Nouns")
verbs = ("Verbs")
adjectives = ("Adjectives")
adverbs = ("Adverbs")
print("\nHere some defintions of Nouns, Verbs, Adverbs, and Adjectives in case you need a friendly reminder:")
print("\n"+ magenta(nouns) +"- a noun is the name of a person, place, or thing.")
print("\n"+ magenta(verbs) +"- are an action word such as run, jump, and swim.")
print("\n"+ magenta(adjectives) +" - describe a person, place, or thing. Some examples are short, tall, happy, soft, and smooth.")
print("\n"+ magenta(adverbs) +"- describe in what way someone does something. For example someone could be running quickly, slowly, or carefully.")

input("\nPress Enter to continue to the instructions.")

print("\nInstructions on how to play our mad libs story generator.")
print("\n1. The program will provide you a story randomly and give you questions based on that story. Provide nouns, verbs, and etc to the provided blanks given by the question. ")
print("\n2. You will not be given the story immediately, but the questions will hint on what you might need to type inside of the blank space so pay close attention.")
print("\n3. The questions will be highlighted in red while your answers will be in green. ")
print("\n4. The fourth and final rule is to enjoy the story! ")

input("\nPress Enter to continue to the story making process!")










def minecraft_story() -> str:
  print(cyan("\nBuilding my House in Minecraft "))
  username=input("\nWhat is your Username in Minecraft? ")
  biome =input("\nWhat is your favorite biome in Minecraft? ")
  block =input("\nWhat block would you like to build your house with? ")

  print("\nMy username is "+ green(username) +" I started my first day on minecraft today.")
  print("My goal is to build a nice house in the "+ green(biome)+".")
  print("First things first I need to gather "+ green(block)+" to build my new house with.")
  print("Nice! I now have all I need.")
  print("Time to go search for a/an "+ green(biome)+" to build my new house in.")
  print("Yes! I found it a/an "+ green(biome)+" I can finally build my dream house time to start building!")
  print("It's done my minecraft house made of "+ green(block)+" is built!")
  print("I am so proud of myself for building this house.") 





def pirate_story() -> str:
  print(yellow("\nTreasue Hunt\n "))
  pirate_name = input(red("What is your Captain's name? "))
  ship_name = input(red("What is the name of your ship? "))
  treasure = input(red("What is the treasure you are seeking? "))
  adjective = input(red("Choose an adjective to call your crewmates. "))
  adverb = input(red("Choose an adverb on how you want your crewmates to finish a task."))

  print("\nShiver me timbers! Cap'n "+ green(pirate_name) +" land ahoy North East of our current waters!\nAye I can see the X from here.\nListen here you scallywags all hands on deck!\nWe set sail our ole "+ green(ship_name) +" on her course to that island!\nYou hear me?!\nAye Cap'n!\nAlright you "+ green(adjective) +" landlubbers the "+ green(treasure) +" is/are somewhere on this beach so start digging "+ green(adverb) +"!\nCap'n we dug up something over here!\nAh finally after all this time I found it.\nRejoice me hearties we have found the "+ green(treasure) +" were going to be rich!\nStart loading up ole "+ green(ship_name) +" with our booty and let us celebrate on our glorious treasure hunt with a feast fit for a pirate!")

def random_story()-> list:
  story = [minecraft_story, pirate_story]
  chosen_story =random.choice(story)
  chosen_story()
random_story()


while True:
    a = input("Do you want to play again yes/no? ")
    if a=="yes":
      random_story()
    elif a=="no":
      print("Thank you for playing!!")
      break
    else:
      print("Enter either yes/no")
