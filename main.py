#-----------------------------------------------------------
# Title: RPG game class
# Class: CS 30
# Date: May 1rst, 2023
# Coders Name: Deepash Sunwar
# Version: 4
#-----------------------------------------------------------
'''
Current Assignment: RPG game class

This program is a simple game where to win the user needs to go to all the rooms,
the user is able to collect items, talk with 'enemies' and is always allowed to quit.
'''

# Importing all objects
from player import Player
from room_map import rooms
from game_info import Game_info

# Initilizing the objects
game_info = Game_info(rooms)
player = Player(input("What is your name: "), "main")
game_info.line_break()

# Printing the introduction
print(
  f"""Welcome {player.name.capitalize()}! To win this game, you have to go in each room and explore it.
at any point of the game you want to quit, just press "q" and enter.""")

game_info.line_break()

# allows me to quit whenever I set this to true
game_on = True

# The main gamee loop
while game_on:
  # Every time the loop restarts it checks if the user has checked all room
  if game_info.win():
    game_info.print_game_menu()
    user_action_choice = input("What action would you like to do: ").lower()
    game_info.line_break()
    # IF the user decides they want to move to a different location
    if user_action_choice == "move":
      game_info.print_move_actions()
      while True:
        game_info.line_break()
        user_move_choice = input("Where would you like to go: ").lower()
        if user_move_choice in ['north', 'east', 'south', 'west']:
          player.move(user_move_choice)
          game_info.print_description(player.current_location)
          break
        elif user_move_choice == 'q':
          print("Thank you for playing!")
          game_on = False
          break
        else:
          print("Please give a valid direction!")
          continue

    # If the user wants to look around it prints out the 'enemy's' greet
    elif user_action_choice == "look":
      game_info.print_look_action(player.current_location)
      game_info.line_break()

    # It checks for the items in the room and adds it to the players inventory
    elif user_action_choice == "inspect":
      game_info.print_items(player.current_location)
      game_info.line_break()
      player.pick_up_items(rooms[player.current_location]['item'])
      rooms[player.current_location]['item'] = 'none'

    # prints the user current inventory

    elif user_action_choice == "inventory":
      game_info.line_break()
      game_info.print_inventory(player.inventory)
      game_info.line_break()

    # if the user wants to quit it breaks out of loop

    elif user_action_choice == "q":
      print("Thank you for playing!")
      break

    # if the user doesn't enter a valid action it asks to enter a valid one
    else:
      print("Please enter a valid action!")
      game_info.line_break()

  # If the user wins the game this runs
  else:
    game_info.line_break()
    print("Thank you for playing!, you have explored all the locations!")
    game_on = False
