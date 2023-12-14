import item.room
import item.door
import item.torch
import item.musicstring
from item.init_assets import *
from item.traps import *
from item.boss import *
from item.cutscene import *

intro = Cutscene()
transition_to_game = Cutscene()
transition_to_game.audio = 0
transition_to_game.limit = 30
transition_to_game.warp_player = 0
transition_to_game.give_control = 0

#---- STRINGS ----#

string1 = item.musicstring.String(  8, 53)
string2 = item.musicstring.String(138, 68)

#----- ROOMS -----#
# NAME: room_roomID

room0  = item.room.Room(room0_sprite,   0,    0,   0)
room1  = item.room.Room(room1_sprite,  40,  162,   1)
room2  = item.room.Room(room2_sprite,  60,  162,   2)
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

door2U  = item.door.Door( 67, 166, 1,  2,  room3)

door3U  = item.door.Door( 67, 136, 1,  3,  room4)
door3D  = item.door.Door( 67, 157, 4,  3,  room2)

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

torch1_1  = item.torch.Torch( 50, 164)

torch2_1  = item.torch.Torch( 70, 164)

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


#---- CONVEYOR BELTS ----#
# NAME: c + direction + conveyorID + roomID
# ex: cD1_3

cU1_5 = conveyorBelt(32,117,1)
cU2_5 = conveyorBelt(32,118,1)
cU3_5 = conveyorBelt(32,119,1)
cU4_5 = conveyorBelt(32,120,1)
cU5_5 = conveyorBelt(32,121,1)
cU6_5 = conveyorBelt(32,122,1)
cU7_5 = conveyorBelt(32,123,1)
cU8_5 = conveyorBelt(32,124,1)
cU9_5 = conveyorBelt(32,125,1)
cU10_5 = conveyorBelt(33,117,1)
cU11_5 = conveyorBelt(33,118,1)
cU12_5 = conveyorBelt(33,119,1)
cU13_5 = conveyorBelt(33,120,1)
cU14_5 = conveyorBelt(33,121,1)
cU15_5 = conveyorBelt(33,122,1)
cU16_5 = conveyorBelt(33,123,1)
cU17_5 = conveyorBelt(33,124,1)
cU18_5 = conveyorBelt(33,125,1)

cR1_5 = conveyorBelt(39,116,3)
cR2_5 = conveyorBelt(39,117,3)
cR3_5 = conveyorBelt(39,118,3)
cR4_5 = conveyorBelt(39,119,3)
cR5_5 = conveyorBelt(39,120,3)
cR6_5 = conveyorBelt(39,121,3)
cR7_5 = conveyorBelt(39,122,3)
cR8_5 = conveyorBelt(39,123,3)
cR9_5 = conveyorBelt(39,124,3)
cR10_5 = conveyorBelt(40,117,3)
cR11_5 = conveyorBelt(40,118,3)
cR12_5 = conveyorBelt(40,119,3)
cR13_5 = conveyorBelt(40,120,3)
cR14_5 = conveyorBelt(40,121,3)
cR15_5 = conveyorBelt(40,122,3)
cR16_5 = conveyorBelt(40,123,3)
cR17_5 = conveyorBelt(40,124,3)
cR18_5 = conveyorBelt(40,116,3)

room5conveyors = [cU1_5,cU2_5,cU3_5,cU4_5,cU5_5,cU6_5,cU7_5,cU8_5,cU9_5,
                  cU10_5,cU11_5,cU12_5,cU13_5,cU14_5,cU15_5,cU16_5,cU17_5,cU18_5,
                  cR1_5,cR2_5,cR3_5,cR4_5,cR5_5,cR6_5,cR7_5,cR8_5,cR9_5,
                  cR10_5,cR11_5,cR12_5,cR13_5,cR14_5,cR15_5,cR16_5,cR17_5,cR18_5]

#---- SPIKE TRAPS ----#
# NAME: spk + roomID_TrapID

spk1_5 = spikeTrap(30,117)
spk2_5 = spikeTrap(30,118)
spk3_5 = spikeTrap(30,119)
spk4_5 = spikeTrap(30,120)
spk5_5 = spikeTrap(30,121)
spk6_5 = spikeTrap(30,122)
spk7_5 = spikeTrap(30,123)
spk8_5 = spikeTrap(30,124)
spk10_5 = spikeTrap(34,117)
spk11_5 = spikeTrap(34,118)
spk12_5 = spikeTrap(34,119)
spk13_5 = spikeTrap(34,120)
spk14_5 = spikeTrap(34,121)
spk15_5 = spikeTrap(34,122)
spk16_5 = spikeTrap(34,123)
spk17_5 = spikeTrap(34,124)
spk19_5 = spikeTrap(36,124)
spk20_5 = spikeTrap(38,124)

room5spikes = [spk1_5,spk2_5,spk3_5,spk4_5,spk5_5,spk6_5,spk7_5,spk8_5,spk10_5,
               spk11_5,spk12_5,spk13_5,spk14_5,spk15_5,spk16_5,spk17_5,spk19_5,spk20_5]

spk1_6 = spikeTrap(30,97)
spk2_6 = spikeTrap(30,98)
spk3_6 = spikeTrap(30,99)
spk4_6 = spikeTrap(30,100)
spk5_6 = spikeTrap(30,101)
spk6_6 = spikeTrap(30,102)
spk7_6 = spikeTrap(26,99)
spk8_6 = spikeTrap(26,100)
spk9_6 = spikeTrap(26,101)
spk10_6 = spikeTrap(26,102)
spk11_6 = spikeTrap(26,103)
spk12_6 = spikeTrap(26,104)

room6spikes = [spk1_6,spk2_6,spk3_6,spk4_6,spk5_6,spk6_6,spk7_6,spk8_6,spk9_6,spk10_6,spk11_6,spk12_6]

#---- FIRE TRAPS ----#
# NAME: fire + roomID_TrapID

fire1_5 = wallTrap(32,126,'d')

fire1_7 = wallTrap(16,100,'r')
fire2_7 = wallTrap(16,96,'r')
fire3_7 = wallTrap(2,98,'l')
fire4_7 = wallTrap(2,94,'l')

room7fire = [fire1_7,fire2_7,fire3_7,fire4_7]


boss = item.boss.Boss( 67, 139) 