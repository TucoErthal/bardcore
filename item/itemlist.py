import item.room
import item.door
import item.torch
from item.init_assets import *

from item.traps import *

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


room1  = item.room.Room(room1_sprite, 32, 22, 1)
room2  = item.room.Room(room2_sprite, 0 , 29, 2)
room3  = item.room.Room(room3_sprite, 58, 22, 3)
room4  = item.room.Room(room4_sprite, 35, 0 , 4)
room5  = item.room.Room(room5_sprite, 1 , 41, 5)
room6  = item.room.Room(room6_sprite, 23, 49, 6)



#----- DOORS -----#
# NAME: doorIDdirection
# U: UP, L: LEFT, R: RIGHT, D: DOWN
# params: (x, y, direction, ID, target room)

door1U = item.door.Door(39, 26, 1, 1, room4)
door1L = item.door.Door(34, 35, 2, 1, room2)
door1R = item.door.Door(53, 30, 3, 1, room3)


door2R = item.door.Door(27, 35, 3, 2, room1)
door2D = item.door.Door(10, 36, 4, 2, room5)


door3L = item.door.Door(60, 30, 2, 3, room1)


door4D = item.door.Door(39, 17, 4, 4, room1)


door5U = item.door.Door(10, 45, 1, 5, room2)
door5R = item.door.Door(18, 59, 3, 5, room6)


door6L = item.door.Door(25, 59, 2, 6, room5)

#---- TORCHES ----#
# NAME: torch_roomID_torchID


torch1_1 = item.torch.Torch(35,24)
torch1_2 = item.torch.Torch(42,24)
torch1_3 = item.torch.Torch(49,24)

torch2_1 = item.torch.Torch(3,31)
torch2_2 = item.torch.Torch(8,31)
torch2_3 = item.torch.Torch(13,31)
torch2_4 = item.torch.Torch(18,31)
torch2_5 = item.torch.Torch(23,31)

torch3_1 = item.torch.Torch(60,24)
torch3_2 = item.torch.Torch(67,24)

torch4_1 = item.torch.Torch(38,2)

torch5_1 = item.torch.Torch(4,43)
torch5_2 = item.torch.Torch(14,43)

torch6_1 = item.torch.Torch(26,51)
torch6_2 = item.torch.Torch(31,51)
torch6_3 = item.torch.Torch(45,51)
torch6_4 = item.torch.Torch(50,51)


#---- SPIKE TRAPS ----#
# NAME: spkTrap_roomID_TrapID

spkTrap1_1 = item.traps.spikeTrap(40,30)

wallTrapL = item.traps.WallTrap(34, 39, 'l')
wallTrapD = item.traps.WallTrap(36, 42, 'd')
wallTrapU = item.traps.WallTrap(36, 35, 'u')
wallTrapR = item.traps.WallTrap(40, 39, 'r')