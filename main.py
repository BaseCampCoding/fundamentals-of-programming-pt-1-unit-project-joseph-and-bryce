import random
import simple_colors
from simple_colors import *
import art
from art import *
mad_libs = text2art("Random\nMad Libs")
print(mad_libs)      

print("Hello user welcome to Bryce and Joseph's custom Mad Lib!")
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
print(green("\nInstructions on how to play our mad libs story generator."))
print("\n1. The program will provide you a story randomly and give you questions based on that story. Provide nouns, verbs, or any words to your liking to the provided blanks given by the question. ")
print("\n2. You will not be given the story immediately, but the questions will hint on what you might need to type inside of the blank space so pay close attention.")
print("\n3. The questions will be highlighted in blue while your answers will be in green within the story. ")
print("\n4. The fourth and final rule is to have fun reading! ")

input("\nPress Enter to continue to the story making process!")




def elevator_story():
  print(magenta("\nWelcome to the Elevator"))
  your_floor = int(input("\nWhat is the floor that you need to get off? "))
  fear = input("\nWhat is your worst fear? ")
  action = input(("\nWhat action would you do if you see your worst fear? "))
  place =input("\nWhat is your favorite place to go? ")
  name = []
  while True:
    response = input("\nName your friends?(q to quit): ")
    if response == 'q':
      break
    name.append(response)
  friend = random.choice(name)
  
  music = input("\nFavorite music? ")
  animal = input("\nWhat is your terrifying animal? ")
  print(magenta("\nWelcome to the Elevator"))
  while True:
    floor = int(input("What floor would like to go? "))
    if floor == your_floor:
      print("YAA you made it to your floor!!")
      break
    elif floor == 1:
      print("\nYou didn't go anywhere\n")
    elif floor == 2:
      print("\nThis floor is having a party and they are playing "+ green(music)+".")
      print("You see one of your friends "+green(friend)+" partying crazy.")
      print("You went back to the elevator becasue you felt confused.\n" )
    elif floor == 3:
      print("\nThis floor is a forest floor and you see your worst fear.")
      print("It's a/an "+ green(fear) +" the first thing you do was to "+ green(action)+".")
      print("Then you ran back to the elevator\n")
    elif floor == 4:
      print("\nThis floor has your favorite place which is/is the "+ green(place)+"\nand you see one of you see "+ green(friend)+" just chillen.")
      print("He sees you and said 'Hey hows it going.'.")
      print("You went back to elevator because you don't understand whats going on?\n")
    elif floor == 5:
      print("\nThis floor is like a jungle and you see "+ green(friend)+" running from "+green(animal)+".")
      print("You quickly shut the elevator door.\n")

    else:
      print("That Number doesn't exist.")







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
  print("Yes! I found it a/an "+ green(biome)+" I can finally build my dream house time to start building before it turns night. ")
  print("It's done my minecraft house made of "+ green(block)+" is built!")
  print("I am so proud of myself for building this house.") 




def pirate_story() -> str:
  print(cyan("\nTreasue Hunt "))
  pirate_name = input(blue("What is your Captain's name? "))
  ship_name = input(blue("What is the name of your ship? "))
  treasure = input(blue("What is the treasure you are seeking? "))
  adjective = input(blue("Choose an adjective to call your crewmates. "))
  adverb = input(blue("Choose an adverb on how you want your crewmates to finish a task. "))

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


def morning_story() -> str:
    print("\nMorning Routine ")
    choice = input("You wake up to the sound of your alarm clock going off where do you go first the bathroom, kitchen, or stay in the bedroom? ")
    if choice == "bedroom":
        print("You decide to change your clothes first in your room before doing anything else. ")
        choice = input("Where do you go now the kitchen or the bathroom? ")
        if choice == "kitchen":
            print("You then head to the kitchen to make some breakfeast and open the fridge to find some eggs and bacon and have a delicious breakfeast. ")
            choice = input("Now that you changed your clothes and had breakfeast do you go to the bathroom yes or no? ")
            if choice == "yes":
                print("You go to the bathroom to brush your teeth and head out of the house for the day. ")
            elif choice == "no":
                print("You decide to stay home instead of heading out looking fresh.")
        elif choice == "bathroom":
            print("You decide to go brush your teeth and tidy up. ")
            choice = input("Now that you have changed your clothes and brushed your teeth do you go eat breakfeast yes or no?")
            if choice == "no":
                print("You head into the kitchen and eat a delicious breakfeast and head out of your home for the day. ")
            elif choice == "yes":
                print("You decide to skip breakfeast because you don't feel hungry.")
    elif choice == "kitchen":
        print("You decide to go make some breakfeast first. ")
        choice = input("Now that you have had a delicious breakfeast where do you go now the bedroom or the bathroom. ")
        if choice == "bedroom":
            print("You make your way to your bedroom to fetch a fresh pair of clothes to change with. ")
            choice = input("Now that you have changed your clothes and ate some breakfeast do you head to the bathroom yes or no? ")
            if choice == "yes":
                print("You brush your teeth and head out of the house for the day. ")
            elif choice == "no":
                print("You decide to skip brushing your teeth this morning and still head out for the day. ")
        if choice == "bathroom":
            print("You make your way to the bathroom to brush your teeth. ")
            choice = input("After you brush your teeth and eat some breakfeast do you head to your room to change clothes yes or no? ")
            if choice == "yes":
                print("You make your way to your room and put on a fresh pair of clothes to start out the day. ")
            elif choice == "no":
                print("You decide to wear the clothes you are currently wearing due to them not smelling too bad. ")
    elif choice == "bathroom":
        print("You decide to go use the bathroom first and brush your teeth. ")
        choice = input("After you brush your teeth where do you go next the kitchen or your bedroom? ")
        if choice == "kitchen":
            print("You head towards the kitchen and make a balanced breakfeast of eggs and bacon. ")
            choice = input("After you brush your teeth and eat some breakfeast do you go to your room to change clothes yes or no? ")
            if choice == "yes":
                print("You decide to change clothes due to them smelling pretty bad and head out of the house for the day. ")
            elif choice == "no":
                print("You decide not to change your clothes or even leave the house that day. ")
        if choice == "bedroom":
            print("You change your clothes in your room do you go to the bathroom next yes or no? ")
            if choice == "yes":
                print("You use the bathroom to brush your teeth and get cleaned up for the day. ")
            elif choice == "no":
                print("You decide to skip going to the bathroom and pop a mint instead and head out for the day. ")






def random_story() -> list:
  story = [minecraft_story, pirate_story, morning_story, elevator_story]
  chosen_story =random.choice(story)
  chosen_story()
random_story()


while True:
    a = input("\nDo you want to play again Y/N? ")
    if a=="Y":
      random_story()
    elif a=="N":
      print("Thank you for playing!!")
      break
    else:
      print("Enter either Y/N")
