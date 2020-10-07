import random
import simple_colors
from simple_colors import *
import art
from art import *
mad_libs = text2art("Mad Libs")
print(mad_libs)      

print("Hello user welcome to Bryce and Joseph's custom Mad Lib!")
input("Press Enter to Continue")
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
print(green("\nInstructions on how to play our mad libs story generator."))
print("\n1. The program will provide you a story randomly and give you questions based on that story. Provide nouns, verbs, or any words to your liking to the provided blanks given by the question. ")
print("\n2. You will not be given the story immediately, but the questions will hint on what you might need to type inside of the blank space so pay close attention.")
print("\n3. The questions will be highlighted in blue while your answers will be in green within the story. ")
print("\n4. The fourth and final rule is to have fun reading! ")

input("\nPress Enter to continue to the story making process!")

def minecraft_story() -> str:
  print(cyan("\nBuilding my House in Minecraft "))
  username = input(blue("\nWhat is your Username in Minecraft? "))
  biome = input(blue("\nWhat is your favorite biome in Minecraft? "))
  block = input(blue("\nWhat block would you like to build your house with? "))
  adjective = input(blue("\nWhat adjective would you like to describe yourself after an accomplishment? "))

  print("\nMy username is "+ green(username) +" I started my first day on minecraft today.")
  print("My goal is to build a nice house in the "+ green(biome)+".")
  print("First things first I need to gather "+ green(block)+" to build my new house with.")
  print("Nice! I now have all I need.")
  print("Time to go search for a/an "+ green(biome)+" to build my new house in.")
  print("Yes! I found it a/an "+ green(biome)+" I can finally build my dream house time to start building "+ green(adverb) +" before it turns night. ")
  print("It's done my minecraft house made of "+ green(block)+" is built!")
  print("I am so proud of myself for building this house.") 

minecraft_story()

def pirate_story() -> str:
  print(cyan("\nTreasue Hunt\n "))
  pirate_name = input(blue("What is your Captain's name? "))
  ship_name = input(blue("What is the name of your ship? "))
  treasure = input(blue("What is the treasure you are seeking? "))
  adjective = input(blue("Choose an adjective to call your crewmates. "))
  adverb = input(blue("Choose an adverb on how you want your crewmates to finish a task."))

  print("\nShiver me timbers! Cap'n "+ green(pirate_name) +" land ahoy North East of our current waters!")
  print("Aye I can see the X from here.")
  print("Listen here you scallywags all hands on deck!")
  print("We set sail our ole "+ green(ship_name) +" on her course to that island!")
  print("You hear me?!")
  print("Aye Cap'n!")
  print("Alright you "+ green(adjective) +" landlubbers the "+ green(treasure) +" is/are somewhere on this here beach so start digging "+ green(adverb) +"!")
  print("Cap'n we dug up something over here!")
  print("Ah finally after all this time I have found it.")
  print("Rejoice me hearties we have found the "+ green(treasure) +" were going to be rich!")
  print("Start loading up ole "+ green(ship_name) +" with our booty and let us celebrate on our glorious treasure hunt with a feast fit for a pirate!")

pirate_story()