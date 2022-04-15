# Importing time and random modules
import time
import random


# Function that will print messages for a user with delay
def print_pause(message):
    print(message)
    time.sleep(1)


# Function that will print intro of the game to a user
def intro():
    print_pause("You find yourself standing in an open field, filled "
                "with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that {character} is somewhere around "
                "here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very "
                "effective) dagger.")


# Function to give user a choice message and call a chooser function
def your_choice():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    chooser(door, cave, "(Please enter 1 or 2).\n")


# Function that takes two other functions and a message to print as parameters
def chooser(func1, func2, message):
    choice = input(message)
    if choice == "1":
        func1()
    elif choice == "2":
        func2()
    else:
        chooser(func1, func2, message)


# Function to ask a user if he/she wants to play again
def play_again():
    choice = input("Would you like to play again? (y/n)")
    if choice == "y":
        print_pause("Excellent! Restarting the game ...")
        play_game()
    elif choice == "n":
        print_pause("Thanks for playing! See you next time.")
    # If answer is not valid we call a function to keep asking a user
    else:
        play_again()


# Function that handles logic when user knoks on a door
def door():
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door "
                f"opens and out steps {character}.")
    print_pause(f"Eep! This is the {character}'s house!")
    print_pause(f"The {character} attacks you!")
    # Message changes if user still doesn't have a new weapon
    if "Desert Eagle" not in backpack:
        print_pause("You feel a bit under-prepared for this, "
                    "with only having a tiny dagger.")
    # Calling chooser function, passing 2 other functions and a message
    chooser(fight, run, "Would you like to (1) fight or (2) run away?\n")


# Function that handles logic when user enters a cave
def cave():
    # If new weapon is in a backpack we print one set of messages
    if "Desert Eagle" in backpack:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all "
                    "the good stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        # Calling function to handle choice logic
        your_choice()
    # Or we print another set of messages, add found weapon to a backpack
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the Desert Eagle .50 Gold Special!")
        print_pause("You discard your silly old dagger and take "
                    "the gun with you.")
        print_pause("You walk back out to the field.")
        backpack.append("Desert Eagle")
        # Calling function to handle choice logic
        your_choice()


# Function that handles logic when user fights
def fight():
    # If user has a new weapon in a backpack we print one set of messages
    if "Desert Eagle" in backpack:
        print_pause(f"As the {character} moves to attack, you "
                    "take out your new Desert Eagle .50 Gold Special.")
        print_pause("The gun shines brightly in your hand as you put "
                    "your finger on a trigger.")
        print_pause(f"But the {character} takes one look at your shiny "
                    "new toy and runs away!")
        print_pause(f"You have rid the town of the {character}. "
                    "You are victorious!")
        # After winning we ask if user wants to play again
        play_again()
    # If user doesn't have a new weapon we print another set of messages
    else:
        print_pause("You do your best...")
        print_pause(f"but your dagger is no match for the {character}.")
        print_pause("You have been defeated!")
        # After losing we ask if user wants to play again
        play_again()


# Function that handles logic when user runs away
def run():
    print_pause("You run back into the field. Luckily, you "
                "don't seem to have been followed.")
    your_choice()


# Creating a main function that starts the game
def play_game():
    # Creating global variables that can be accesed by other functions
    global character
    global backpack
    # Creating list of characters for a game
    characters = ["Vladimir Putin", "Osama bin Laden", "Kim Jong-un",
                  "Omar al-Shishani", "Alexander Lukashenko"]
    # Choosing a random character from a list of characters
    character = random.choice(characters)
    # List to store a new weapon
    backpack = []
    # Calling intro to start a game
    intro()
    # Calling function to prompt user to make a choice and call other functions
    your_choice()


# Calling a main play_game function that starts the game
play_game()
