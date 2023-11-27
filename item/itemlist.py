import item.room
import item.door
import item.torch
from item.init_assets import *
t = 16

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


room_1  = item.room.Room(first_room_sprite, 496, 336)
room_2  = item.room.Room(second_room_sprite, 0, 448)
room_3  = item.room.Room(third_room_sprite, 896, 336)
room_4  = item.room.Room(fourth_room_sprite, 608, 0)



#----- DOORS -----#
# NAME: room_roomID_door_direction

room_1_door_up    = item.door.Door(616, 400, 400, 400, door_sprite, door_open_sprite)
room_1_door_left  = item.door.Door(256, 256, 400, 400, door_left_sprite, door_left_sprite)
room_1_door_right = item.door.Door(256, 128, 400, 400, door_right_sprite, door_right_sprite)



#---- TORCHES ----#
# NAME: torch_roomID_torchID


torch_1_1 = item.torch.Torch(544,368)
torch_1_2 = item.torch.Torch(656,368)
torch_1_3 = item.torch.Torch(768,368)