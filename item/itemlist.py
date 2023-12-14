import item.room
import item.door
import item.torch
import item.musicstring
from item.init_assets import *
from item.traps import *
from item.boss import *

#---- STRINGS ----#

string1 = item.musicstring.String(  8, 53)
string2 = item.musicstring.String(138, 68)

#----- ROOMS -----#
# NAME: room_roomID

room3  = item.room.Room(room3_sprite,  59,  132,   3)
room4  = item.room.Room(room4_sprite,  50,  110,   4)
room5  = item.room.Room(room5_sprite,  28,  110,   5)
room6  = item.room.Room(room6_sprite,  22,   92,   6)
room7  = item.room.Room(room7_sprite,   0,   87,   7)
room8  = item.room.Room(room8_sprite,   0,   46,   8)
room9  = item.room.Room(room9_sprite,   86, 112,   9)
room10 = item.room.Room(room10_sprite, 130, 108,  10)
room11 = item.room.Room(room11_sprite, 124,  86,  11)
room12 = item.room.Room(room12_sprite, 132,  61,  12)
room13 = item.room.Room(room13_sprite,  56,  90,  13)
room14 = item.room.Room(room14_sprite,  52,  46,  14)
room15 = item.room.Room(room15_sprite,  54,  18,  15)
room16 = item.room.Room(room16_sprite,  59,   0,  16)



#----- DOORS -----#
# NAME: room_roomID_door_direction
# 1 = UP, 2 = LEFT, 3 = RIGHT, 4 = DOWN


door3U  = item.door.Door( 67, 136, 1,  3,  room4)

door4U  = item.door.Door( 66, 114, 1,  4, room13)
door4L  = item.door.Door( 52, 120, 2,  4,  room5)
door4R  = item.door.Door( 81, 120, 3,  4,  room9)
door4D  = item.door.Door( 67, 127, 4,  4,  room3)

door5U  = item.door.Door( 37, 114, 1,  5,  room6)
door5R  = item.door.Door( 45, 120, 3,  5,  room4)

door6L  = item.door.Door( 24, 103, 2,  6,  room7)
door6D  = item.door.Door( 37, 105, 4,  6,  room5)

door7U  = item.door.Door(  9,  91, 1,  7,  room8)
door7R  = item.door.Door( 17, 103, 3,  7,  room6)

door8D  = item.door.Door(  9,  82, 4,  8,  room7)

door9L  = item.door.Door( 88, 120, 2,  9,  room4)
door9R  = item.door.Door(125, 122, 3,  9, room10)

door10U = item.door.Door(138, 112, 1, 10, room11)
door10L = item.door.Door(132, 122, 2, 10,  room9)

door11U = item.door.Door(138,  90, 1, 11, room12)
door11D = item.door.Door(138, 103, 4, 11, room10)

door12D = item.door.Door(138,  81, 4, 12, room11)

door13U = item.door.Door( 66,  94, 1, 13, room14, 'string')
door13D = item.door.Door( 66, 105, 4, 13,  room4)

door14U = item.door.Door( 66,  50, 1, 14, room15)
door14D = item.door.Door( 66,  85, 4, 14, room13)

door15U = item.door.Door( 66,  22, 1, 15, room16)
door15D = item.door.Door( 66,  41, 4, 15, room14)

door16D = item.door.Door( 66,  13, 4, 16, room15)




#---- TORCHES ----#
# NAME: torch + roomID_torchID

torch3_1  = item.torch.Torch( 62, 134)
torch3_2  = item.torch.Torch( 70, 134)

torch4_1  = item.torch.Torch( 53, 112)
torch4_2  = item.torch.Torch( 58, 112)
torch4_3  = item.torch.Torch( 72, 112)
torch4_4  = item.torch.Torch( 77, 112)

torch5_1  = item.torch.Torch( 31, 112)
torch5_2  = item.torch.Torch( 41, 112)

torch6_1  = item.torch.Torch( 25,  94)
torch6_2  = item.torch.Torch( 30,  94)
torch6_3  = item.torch.Torch( 36,  94)
torch6_4  = item.torch.Torch( 41,  94)

torch7_1  = item.torch.Torch(  4,  89)
torch7_2  = item.torch.Torch( 12,  89)

torch8_1  = item.torch.Torch(  3,  48)
torch8_2  = item.torch.Torch( 11,  48)

torch9_1  = item.torch.Torch( 90, 114)
torch9_2  = item.torch.Torch( 96, 114)
torch9_3  = item.torch.Torch(102, 114)
torch9_4  = item.torch.Torch(108, 114)
torch9_5  = item.torch.Torch(114, 114)
torch9_6  = item.torch.Torch(120, 114)

torch10_1 = item.torch.Torch(135, 110)
torch10_2 = item.torch.Torch(145, 110)

torch11_1 = item.torch.Torch(127,  88)
torch11_2 = item.torch.Torch(132,  88)
torch11_3 = item.torch.Torch(142,  88)
torch11_4 = item.torch.Torch(147,  88)

torch12_1 = item.torch.Torch(134,  63)
torch12_2 = item.torch.Torch(140,  63)

torch14_1 = item.torch.Torch( 55,  48)
torch14_2 = item.torch.Torch( 60,  48)
torch14_3 = item.torch.Torch( 70,  48)
torch14_4 = item.torch.Torch( 75,  48)

torch15_1 = item.torch.Torch( 57,  20)
torch15_2 = item.torch.Torch( 62,  20)
torch15_3 = item.torch.Torch( 68,  20)
torch15_4 = item.torch.Torch( 73,  20)

torch16_1 = item.torch.Torch( 62,   2)
torch16_2 = item.torch.Torch( 68,   2)













'''
#---- SPIKE TRAPS ----#
# NAME: spkTrap_roomID_TrapID

spkTrap1_1 = item.traps.spikeTrap(40,30)

wallTrapL = item.traps.WallTrap(34, 39, 'l')
wallTrapD = item.traps.WallTrap(36, 42, 'd')
wallTrapU = item.traps.WallTrap(36, 35, 'u')
wallTrapR = item.traps.WallTrap(40, 39, 'r')


#---- CONVEYOR BELTS ----#
# NAME: c + direction + roomIDs
'''
boss = item.boss.Boss( 67, 139) 