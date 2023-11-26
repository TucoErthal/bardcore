import room
import door
from init_assets import *

first_room = room.generateRoom(first_room_sprite)
#second_room = room.generateRoom()


first_room_door = door.generateDoor(128, 128, 0, 0, door_sprite, door_open_sprite)