from simple_colors import *

print("Hello user elcome to Bryce and Joseph's custom Mad Lib!")
nouns = ("Nouns")

print("\nHere some defintions of Nouns, Verbs, Adverbs, and Adjectives in case you need a friendly reminder:")
print("\n"+ nouns +"- a noun is the name of a person, place, or thing.")
print("\nVerbs - are an action word such as run, jump, and swim.")
print("\nAdjectives - describe a person, place, or thing. Some examples are short, tall, happy, soft, and smooth.")
print("\nAdverbs - describe in what way someone does something. For example someone could be running quickly, slowly, or carefully.")

input("\nPress Enter to continue to the instructions.")

print("\nInstructions on how to play our mad libs story generator.")
print("\n1. The program will provide you a story randomly and give you questions based on that story. Provide nouns, verbs, and etc to the provided blanks given by the question. ")
print("\n2. You will not be given the story immediately, but the questions will hint on what you might need to type inside of the blank space so pay close attention.")
print("\n3. The questions will be highlighted in red while your answers will be in green. ")
print("\n4. The fourth and final rule is to enjoy the story! ")

input("\nPress Enter to continue to the story making process!")












def minecraft_story() -> str:
  print(yellow("\nBuilding my House in Minecraft\n "))
  username=input(red("\nWhat is your Username in Minecraft? "))
  biome =input(red("\nWhat is your favorite biome in Minecraft? "))
  block =input(red("\nWhat block would you like to build your house with? "))

  print("\nMy username is "+ green(username) +" I started my first day on minecraft today.\nMy goal is to build a nice house in the "+ green(biome)+".\nFirst things first I need to gather "+ green(block)+" to build my new house with.\nNice! I now have all I need.\nTime to go search for a/an "+ green(biome)+" to build my new house in.\nYes! I found it a/an "+ green(biome)+" I can finally build my dream house time to start building!\nIt's done my minecraft house made of "+ green(block)+" is built!\nI am so proud of myself for building this house.")   

minecraft_story()