import item.room
import item.door
import item.torch
from item.init_assets import *

# REMEMBER!!! When defining assets in a room, such as torches or doors,
# first identify where in the (x, y) plane they will go, then sum by the
# room's (x, y) values!
# EX: torch goes on 64, 64 in room A, and room A is in 320, 320.
# Simply place torch on 384, 384! Voila!


#----- ROOMS -----#
# NAME: room_roomID




#----- DOORS -----#
# NAME: room_roomID_door_direction




#---- TORCHES ----#
# NAME: torch_roomID_torchID







# TEMPORARY -> ONLY FOR THE DEMO #


#----- ROOMS -----#
# NAME: room_roomID


room1  = item.room.Room(first_room_sprite , 31, 21, 1)
room2  = item.room.Room(second_room_sprite, 0 , 28, 2)
room3  = item.room.Room(third_room_sprite , 56, 21, 3)
room4  = item.room.Room(fourth_room_sprite, 38, 0 , 4)



#----- DOORS -----#
# NAME: doorIDdirection
# U: UP, L: LEFT, R: RIGHT, D: DOWN

door1U    = item.door.Door(38, 25, 42, 15, door_sprite, door_open_sprite, 1, room4)
door1L  = item.door.Door(33, 34, 25, 34, door_left_sprite, door_left_sprite, 1, room2)
door1R = item.door.Door(52, 29, 60, 29, door_right_sprite, door_right_sprite, 1, room3)

door2R = item.door.Door(27, 34, 35, 34, door_right_sprite, door_right_sprite, 2, room1)

door3L = item.door.Door(58, 29, 50, 29, door_left_sprite, door_left_sprite, 3, room1)

door4D = item.door.Door(42, 17, 38, 28, door_down_sprite, door_down_sprite, 4, room1)

#---- TORCHES ----#
# NAME: torch_roomID_torchID


torch1_1 = item.torch.Torch(34,23)
torch1_2 = item.torch.Torch(41,23)
torch1_3 = item.torch.Torch(48,23)

torch2_1 = item.torch.Torch(3,30)
torch2_2 = item.torch.Torch(8,30)
torch2_3 = item.torch.Torch(13,30)
torch2_4 = item.torch.Torch(18,30)
torch2_5 = item.torch.Torch(23,30)

torch3_1 = item.torch.Torch(58,23)
torch3_2 = item.torch.Torch(65,23)

torch4_1 = item.torch.Torch(41,2)