from character import Character
from room_map import rooms

class Player(Character):

  def __init__(self, name, current_location):
    """
        empty inventory, and inheriting current location and name from base class
        """
    super().__init__(name, current_location)
    self.inventory = []

  def pick_up_items(self, item):
    """
        resposible for collectiing items from room
        """
    if item != "none":
      self.inventory.append(item)

  def move(self, location):
    """
        Sets the current location to new location and makes it true that user went to room
        """
    self.current_location = location
    rooms[location]['checked'] = True