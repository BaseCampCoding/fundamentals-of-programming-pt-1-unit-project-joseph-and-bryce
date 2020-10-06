## Description and Motivation
In this project, Bryce and I want to build a mad libs generator game with a twist. We still want to use the basic style of mad libs, but instead of telling the user the story
right up front we are going to start off with questions about each individual story. More specifically Bryce and I want to reference http://madlibs.bostonchildrensmuseum.org/.
For example the user chooses the story they want in mad libs, but in our twist of the game it gives you the input first, and then the story. Basically you will be asked input
first and then you will see the story that the game chooses out of a selection of stories randomly. Our goal for the project is to create a program where input is asked first
and then a story is produced randomly from a selected list where the user can enjoy reading a story they basically made. We do intend in the future if possible to add in audio
while the user is on a selected story.


## Prior Art
There are a lot of story based games out there dealing with words that you either input or receive from an output, but Bryce and I want to take it a different direction.
We want to apply the mad libs style to our program, but instead of the user choosing the story our program will choose the story randomly and hint the user on what the 
story might be about with the questions the user is asked. The point of our program is to just build something mysterious and fun for people to enjoy with familiar elements
from mad libs, but with our own twist.


## Core User Workflows
- Creating the mad lib - The user will be input any nouns, adjectives, adverbs, or verbs from the provided questions asked to create their own story that they can enjoy
provided by the program from a randomly selected list.
- Viewing the mad lib - Once the user has provided the input they want they get the pleasure of reading the story based off of their input and can try again if they so wish
which will again select a story from the list randomly.


## Daily Goals
#### Tuesday: A user should be able to put input into the first story
Our first goal is to greet the user with the definitions of noun, verb, adjective, and adverb. Once that is complete we want to create the first story with input usage from the user so they can basically use any type of word they want that falls into the blank space. This involves us to do a lot of testing to see if the input works with string concatenation.

#### Wednesday: A user should be able to choose to play again or quit and the program should call upon one of the two stories randomly
Once we have the code to make a story work with user input we need to create a second story using similar coding and put it into a list to call upon it randomly. Once we accomplish that we need to add in a while loop to ask the user if they want to play again or quit.

#### Thursday: The user should be able to be given at least 3 stories with the decision of choosing to quit or play again
Once we are successfully able to create three stories the program should be able to randomly call upon one of the stories if the user wishes for it to happen otherwise the user can quit. As a bonus that is optional Bryce and I are going to try and implement audio while the user is in one of the stories giving an extra twist of the original mad libs.


## Students
- Joseph
- Bryce


## GitHub Repository
https://github.com/BaseCampCoding/fundamentals-of-programming-pt-1-unit-project-joseph-and-bryce
