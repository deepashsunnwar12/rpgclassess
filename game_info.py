from room_map import rooms
class Game_info:
  """
    Responsible for printing out game information
    """

  def __init__(self, room_map):
    self.room_map = room_map

  def print_game_menu(self):
    """
        Prints the basic game menu
        """
    print("★ Look")
    print("★ Inspect")
    print("★ Move")
    print("★ Inventory")

  def print_move_actions(self):
    """
        prints the menu for move
        """
    for locations in rooms:
      if locations == 'main':
        continue
      else:
        print(
          f"★ ({locations.capitalize()}) The {self.room_map[locations]['name']}"
        )

  def print_look_action(self, location):
    """
        Checks if their is a "enemy" in the room, if there is someone there it greets them
        """
    if self.room_map[location]['enemy'] == "none":
      print("There is no one here!")
    else:
      print(
        f"You've found {self.room_map[location]['enemy'].capitalize()} and he says hi!"
      )

  def print_inventory(self, inventory):
    """
        checks if the inventory is empty or not and according to that it prints
        out the inventory
        """
    if inventory != []:
      print("You have the following items in your inventory:")
      for item in inventory:
        print(f"★ {item.capitalize()}")
    else:
      print("You have no items in your inventory yet.")

  def print_description(self, location):
    """
    prints the location description
    """
    print(self.room_map[location]['description'])

  def print_items(self, location):
    """
    prints the item in the current location
    """
    if self.room_map[location]['item'] == "none":
      print("There are no items in this location!")
    else:
      print("The following item has been added to your inventory:")
      print(f"★ {self.room_map[location]['item']}")

  def win(self):
    """
    Checks if a win ever happens, which can only happen if all rooms are checked out
    """
    win_or_not = []
    for location in self.room_map:
      if self.room_map[location]['item'] != 'none':
        win_or_not.append(True)
      win_or_not.append(self.room_map[location]['checked'])

    return False in win_or_not

  def line_break(self):
    """
    Makes it easier to see
    """ 
    print("===================================")
