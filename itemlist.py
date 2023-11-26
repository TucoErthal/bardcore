import room
import door
import torch
from init_assets import *


# REMEMBER!!! When defining assets in a room, such as torches or doors,
# first identify where in the (x, y) plane they will go, then sum by the
# room's (x, y) values!
# EX: torch goes on 64, 64 in room A, and room A is in 320, 320.
# Simply place torch on 384, 384! Voila!

first_room  = room.generateRoom(first_room_sprite,496,336)
second_room = room.generateRoom(second_room_sprite, 0, 448)
third_room  = room.generateRoom(third_room_sprite, 896, 336)
fourth_room = room.generateRoom(fourth_room_sprite, 608, 0)


first_room_door_up = door.generateDoor(616, 400, 400, 400, door_sprite, door_open_sprite)
first_room_door_left = door.generateDoor(256, 256, 400, 400, door_left_sprite, door_left_sprite)
first_room_door_right = door.generateDoor(256, 128, 400, 400, door_right_sprite, door_right_sprite)

torch_A = torch.Torch(544,368)
torch_B = torch.Torch(656,368)
torch_C = torch.Torch(768,368)