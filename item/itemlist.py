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
room14 = item.room.Room(room14_sprite,  52,  64,  14)
room15 = item.room.Room(room15_sprite,  54,  36,  15)
room16 = item.room.Room(room16_sprite,  59,  18,  16)



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

door14U = item.door.Door( 66,  68, 1, 14, room15)
door14D = item.door.Door( 66,  85, 4, 14, room13)

door15U = item.door.Door( 66,  40, 1, 15, room16)
door15D = item.door.Door( 66,  59, 4, 15, room14)

door16D = item.door.Door( 66,  31, 4, 16, room15)




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

torch14_1 = item.torch.Torch( 55,  66)
torch14_2 = item.torch.Torch( 60,  66)
torch14_3 = item.torch.Torch( 70,  66)
torch14_4 = item.torch.Torch( 75,  66)

torch15_1 = item.torch.Torch( 57,  38)
torch15_2 = item.torch.Torch( 62,  38)
torch15_3 = item.torch.Torch( 68,  38)
torch15_4 = item.torch.Torch( 73,  38)

torch16_1 = item.torch.Torch( 62,  20)
torch16_2 = item.torch.Torch( 68,  20)


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

cL1_11 = conveyorBelt(88,118,2)
cL2_11 = conveyorBelt(89,118,2)
cL3_11 = conveyorBelt(90,118,2)
cL4_11 = conveyorBelt(91,118,2)
cL5_11 = conveyorBelt(92,118,2)
cL6_11 = conveyorBelt(93,118,2)
cL7_11 = conveyorBelt(94,118,2)
cL8_11 = conveyorBelt(95,118,2)
cL9_11 = conveyorBelt(96,118,2)
cL10_11 = conveyorBelt(97,118,2)
cL11_11 = conveyorBelt(98,118,2)
cL12_11 = conveyorBelt(99,118,2)
cL13_11 = conveyorBelt(100,118,2)
cL14_11 = conveyorBelt(101,118,2)
cL15_11 = conveyorBelt(102,118,2)
cL16_11 = conveyorBelt(103,118,2)
cL17_11 = conveyorBelt(104,118,2)
cL18_11 = conveyorBelt(105,118,2)
cL19_11 = conveyorBelt(106,118,2)
cL20_11 = conveyorBelt(107,118,2)
cL21_11 = conveyorBelt(108,118,2)
cL22_11 = conveyorBelt(109,118,2)
cL23_11 = conveyorBelt(110,118,2)
cL24_11 = conveyorBelt(111,118,2)
cL25_11 = conveyorBelt(112,118,2)
cL26_11 = conveyorBelt(113,118,2)
cL27_11 = conveyorBelt(114,118,2)
cL28_11 = conveyorBelt(115,118,2)
cL29_11 = conveyorBelt(116,118,2)
cL30_11 = conveyorBelt(117,118,2)
cL31_11 = conveyorBelt(118,118,2)
cL32_11 = conveyorBelt(119,118,2)
cL33_11 = conveyorBelt(120,118,2)
cL34_11 = conveyorBelt(121,118,2)
cL35_11 = conveyorBelt(122,118,2)
cL36_11 = conveyorBelt(123,118,2)
cL37_11 = conveyorBelt(124,118,2)
cL38_11 = conveyorBelt(125,118,2)

cL1_11B = conveyorBelt(88,125,2)
cL2_11B = conveyorBelt(89,125,2)
cL3_11B = conveyorBelt(90,125,2)
cL4_11B = conveyorBelt(91,125,2)
cL5_11B = conveyorBelt(92,125,2)
cL6_11B = conveyorBelt(93,125,2)
cL7_11B = conveyorBelt(94,125,2)
cL8_11B = conveyorBelt(95,125,2)
cL9_11B = conveyorBelt(96,125,2)
cL10_11B = conveyorBelt(97,125,2)
cL11_11B = conveyorBelt(98,125,2)
cL12_11B = conveyorBelt(99,125,2)
cL13_11B = conveyorBelt(100,125,2)
cL14_11B = conveyorBelt(101,125,2)
cL15_11B = conveyorBelt(102,125,2)
cL16_11B = conveyorBelt(103,125,2)
cL17_11B = conveyorBelt(104,125,2)
cL18_11B = conveyorBelt(105,125,2)
cL19_11B = conveyorBelt(106,125,2)
cL20_11B = conveyorBelt(107,125,2)
cL21_11B = conveyorBelt(108,125,2)
cL22_11B = conveyorBelt(109,125,2)
cL23_11B = conveyorBelt(110,125,2)
cL24_11B = conveyorBelt(111,125,2)
cL25_11B = conveyorBelt(112,125,2)
cL26_11B = conveyorBelt(113,125,2)
cL27_11B = conveyorBelt(114,125,2)
cL28_11B = conveyorBelt(115,125,2)
cL29_11B = conveyorBelt(116,125,2)
cL30_11B = conveyorBelt(117,125,2)
cL31_11B = conveyorBelt(118,125,2)
cL32_11B = conveyorBelt(119,125,2)
cL33_11B = conveyorBelt(120,125,2)
cL34_11B = conveyorBelt(121,125,2)
cL35_11B = conveyorBelt(122,125,2)
cL36_11B = conveyorBelt(123,125,2)
cL37_11B = conveyorBelt(124,125,2)
cL38_11B = conveyorBelt(125,125,2)

cD1_9 = conveyorBelt(101,121,4)
cD2_9 = conveyorBelt(101,122,4)
cD3_9 = conveyorBelt(101,123,4)
cD4_9 = conveyorBelt(101,124,4)
cD5_9 = conveyorBelt(102,121,4)
cD6_9 = conveyorBelt(102,122,4)
cD7_9 = conveyorBelt(102,123,4)
cD8_9 = conveyorBelt(102,124,4)
cD9_9 = conveyorBelt(109,121,4)
cD10_9 = conveyorBelt(109,122,4)
cD11_9 = conveyorBelt(109,123,4)
cD12_9 = conveyorBelt(109,124,4)
cD13_9 = conveyorBelt(110,121,4)
cD14_9 = conveyorBelt(110,122,4)
cD15_9 = conveyorBelt(110,123,4)
cD16_9 = conveyorBelt(110,124,4)
cU1_9 = conveyorBelt(105,119,1)
cU2_9 = conveyorBelt(105,120,1)
cU3_9 = conveyorBelt(105,121,1)
cU4_9 = conveyorBelt(105,122,1)
cU5_9 = conveyorBelt(106,119,1)
cU6_9 = conveyorBelt(106,120,1)
cU7_9 = conveyorBelt(106,121,1)
cU8_9 = conveyorBelt(106,122,1)

# YES I KNOW IT SAYS 11, I CAN'T BOTHER RETYPING EVERYTHING
room9conveyors = [cL1_11,cL2_11,cL3_11,cL4_11,cL5_11,cL6_11,cL7_11,cL8_11,cL9_11,cL10_11,
                  cL11_11,cL12_11,cL13_11,cL14_11,cL15_11,cL16_11,cL17_11,cL18_11,cL19_11,cL20_11,
                  cL21_11,cL22_11,cL23_11,cL24_11,cL25_11,cL26_11,cL27_11,cL28_11,cL29_11,cL30_11,
                  cL31_11,cL32_11,cL33_11,cL34_11,cL35_11,cL36_11,cL37_11,cL38_11,
                  cL1_11B,cL2_11B,cL3_11B,cL4_11B,cL5_11B,cL6_11B,cL7_11B,cL8_11B,cL9_11B,cL10_11B,
                  cL11_11B,cL12_11B,cL13_11B,cL14_11B,cL15_11B,cL16_11B,cL17_11B,cL18_11B,cL19_11B,cL20_11B,
                  cL21_11B,cL22_11B,cL23_11B,cL24_11B,cL25_11B,cL26_11B,cL27_11B,cL28_11B,cL29_11B,cL30_11B,
                  cL31_11B,cL32_11B,cL33_11B,cL34_11B,cL35_11B,cL36_11B,cL37_11B,cL38_11B,
                  cD1_9,cD2_9,cD3_9,cD4_9,cD5_9,cD6_9,cD7_9,cD8_9,
                  cD9_9,cD10_9,cD11_9,cD12_9,cD13_9,cD14_9,cD15_9,cD16_9,
                  cU1_9,cU2_9,cU3_9,cU4_9,cU5_9,cU6_9,cU7_9,cU8_9]

cR1_11C = conveyorBelt(127,93,3)
cR2_11C = conveyorBelt(128,93,3)
cR3_11C = conveyorBelt(129,93,3)
cR4_11C = conveyorBelt(130,93,3)
cR5_11C = conveyorBelt(131,93,3)
cR6_11C = conveyorBelt(132,93,3)
cR7_11C = conveyorBelt(133,93,3)
cR8_11C = conveyorBelt(134,93,3)
cR9_11C = conveyorBelt(135,93,3)
cD1_11C = conveyorBelt(136,93,4)
cD2_11C = conveyorBelt(136,94,4)
cD3_11C = conveyorBelt(136,95,4)
cD4_11C = conveyorBelt(136,96,4)
cD5_11C = conveyorBelt(136,97,4)
cD6_11C = conveyorBelt(136,98,4)
cD7_11C = conveyorBelt(136,99,4)
cD8_11C = conveyorBelt(136,100,4)
cD9_11C = conveyorBelt(136,101,4)
cL1_11C = conveyorBelt(136,102,2)
cL2_11C = conveyorBelt(135,102,2)
cL3_11C = conveyorBelt(134,102,2)
cL4_11C = conveyorBelt(133,102,2)
cL5_11C = conveyorBelt(132,102,2)
cL6_11C = conveyorBelt(131,102,2)
cL7_11C = conveyorBelt(130,102,2)
cL8_11C = conveyorBelt(129,102,2)
cL9_11C = conveyorBelt(128,102,2)
cU1_11C = conveyorBelt(127,102,1)
cU2_11C = conveyorBelt(127,101,1)
cU3_11C = conveyorBelt(127,100,1)
cU4_11C = conveyorBelt(127,99,1)
cU5_11C = conveyorBelt(127,98,1)
cU6_11C = conveyorBelt(127,97,1)
cU7_11C = conveyorBelt(127,96,1)
cU8_11C = conveyorBelt(127,95,1)
cU9_11C = conveyorBelt(127,94,1)

cR1_11D = conveyorBelt(141,102,3)
cR2_11D = conveyorBelt(142,102,3)
cR3_11D = conveyorBelt(143,102,3)
cR4_11D = conveyorBelt(144,102,3)
cR5_11D = conveyorBelt(145,102,3)
cR6_11D = conveyorBelt(146,102,3)
cR7_11D = conveyorBelt(147,102,3)
cR8_11D = conveyorBelt(148,102,3)
cR9_11D = conveyorBelt(149,102,3)
cD1_11D = conveyorBelt(141,93,4)
cD2_11D = conveyorBelt(141,94,4)
cD3_11D = conveyorBelt(141,95,4)
cD4_11D = conveyorBelt(141,96,4)
cD5_11D = conveyorBelt(141,97,4)
cD6_11D = conveyorBelt(141,98,4)
cD7_11D = conveyorBelt(141,99,4)
cD8_11D = conveyorBelt(141,100,4)
cD9_11D = conveyorBelt(141,101,4)
cL1_11D = conveyorBelt(150,93,2)
cL2_11D = conveyorBelt(149,93,2)
cL3_11D = conveyorBelt(148,93,2)
cL4_11D = conveyorBelt(147,93,2)
cL5_11D = conveyorBelt(146,93,2)
cL6_11D = conveyorBelt(145,93,2)
cL7_11D = conveyorBelt(144,93,2)
cL8_11D = conveyorBelt(143,93,2)
cL9_11D = conveyorBelt(142,93,2)
cU1_11D = conveyorBelt(150,102,1)
cU2_11D = conveyorBelt(150,101,1)
cU3_11D = conveyorBelt(150,100,1)
cU4_11D = conveyorBelt(150,99,1)
cU5_11D = conveyorBelt(150,98,1)
cU6_11D = conveyorBelt(150,97,1)
cU7_11D = conveyorBelt(150,96,1)
cU8_11D = conveyorBelt(150,95,1)
cU9_11D = conveyorBelt(150,94,1)

room11conveyors = [cR1_11C,cR2_11C,cR3_11C,cR4_11C,cR5_11C,cR6_11C,cR7_11C,cR8_11C,cR9_11C,
                   cU1_11C,cU2_11C,cU3_11C,cU4_11C,cU5_11C,cU6_11C,cU7_11C,cU8_11C,cU9_11C,
                   cL1_11C,cL2_11C,cL3_11C,cL4_11C,cL5_11C,cL6_11C,cL7_11C,cL8_11C,cL9_11C,
                   cD1_11C,cD2_11C,cD3_11C,cD4_11C,cD5_11C,cD6_11C,cD7_11C,cD8_11C,cD9_11C,

                   cR1_11D,cR2_11D,cR3_11D,cR4_11D,cR5_11D,cR6_11D,cR7_11D,cR8_11D,cR9_11D,
                   cU1_11D,cU2_11D,cU3_11D,cU4_11D,cU5_11D,cU6_11D,cU7_11D,cU8_11D,cU9_11D,
                   cL1_11D,cL2_11D,cL3_11D,cL4_11D,cL5_11D,cL6_11D,cL7_11D,cL8_11D,cL9_11D,
                   cD1_11D,cD2_11D,cD3_11D,cD4_11D,cD5_11D,cD6_11D,cD7_11D,cD8_11D,cD9_11D]


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
spk13_6 = spikeTrap(34,99)
spk14_6 = spikeTrap(34,100)
spk15_6 = spikeTrap(34,101)
spk16_6 = spikeTrap(34,102)
spk17_6 = spikeTrap(34,103)
spk18_6 = spikeTrap(34,104)

room6spikes = [spk1_6,spk2_6,spk3_6,spk4_6,spk5_6,spk6_6,spk7_6,spk8_6,spk9_6,
               spk10_6,spk11_6,spk12_6,spk13_6,spk14_6,spk15_6,spk16_6,spk17_6,spk18_6]

spk1_7 = spikeTrap(3,100)
spk2_7 = spikeTrap(9,100)
spk3_7 = spikeTrap(15,100)
spk4_7 = spikeTrap(7,97)
spk5_7 = spikeTrap(13,97)
spk6_7 = spikeTrap(5,94)
spk7_7 = spikeTrap(11,94)

room7spikes = [spk1_7,spk2_7,spk3_7,spk4_7,spk5_7,spk6_7,spk7_7]

spk1_8 = spikeTrap(2,78)
spk2_8 = spikeTrap(4,78)
spk3_8 = spikeTrap(6,78)
spk4_8 = spikeTrap(8,78)
spk5_8 = spikeTrap(8,77)
spk6_8 = spikeTrap(8,76)
spk7_8 = spikeTrap(12,78)
spk8_8 = spikeTrap(14,78)
spk9_8 = spikeTrap(12,77)
spk10_8 = spikeTrap(14,77)
spk11_8 = spikeTrap(12,76)
spk12_8 = spikeTrap(12,75)
spk13_8 = spikeTrap(12,74)
spk14_8 = spikeTrap(12,73)
spk15_8 = spikeTrap(12,72)
spk16_8 = spikeTrap(10,72)
spk17_8 = spikeTrap(8,72)
spk18_8 = spikeTrap(6,72)
spk19_8 = spikeTrap(12,73)
spk20_8 = spikeTrap(10,73)
spk21_8 = spikeTrap(8,73)
spk22_8 = spikeTrap(6,73)
spk23_8 = spikeTrap(4,68)
spk24_8 = spikeTrap(8,68)
spk25_8 = spikeTrap(12,68)
spk26_8 = spikeTrap(5,63)
spk27_8 = spikeTrap(7,63)
spk28_8 = spikeTrap(9,63)
spk29_8 = spikeTrap(11,63)
spk30_8 = spikeTrap(5,59)
spk31_8 = spikeTrap(7,59)
spk32_8 = spikeTrap(9,59)
spk33_8 = spikeTrap(11,59)
spk34_8 = spikeTrap(5,62)
spk35_8 = spikeTrap(5,61)
spk36_8 = spikeTrap(5,60)
spk37_8 = spikeTrap(11,62)
spk38_8 = spikeTrap(11,61)
spk39_8 = spikeTrap(11,60)

room8spikes = [spk1_8,spk2_8,spk3_8,spk4_8,spk5_8,spk6_8,spk7_8,spk8_8,spk9_8,spk10_8,
               spk11_8,spk12_8,spk13_8,spk14_8,spk15_8,spk16_8,spk17_8,spk18_8,spk19_8,spk20_8,
               spk21_8,spk22_8,spk23_8,spk24_8,spk25_8,spk26_8,spk27_8,spk28_8,spk29_8,spk30_8,
               spk31_8,spk32_8,spk33_8,spk34_8,spk35_8,spk36_8,spk37_8,spk38_8,spk39_8]

spk1_10 = spikeTrap(132,117)
spk2_10 = spikeTrap(134,117)
spk3_10 = spikeTrap(136,117)
spk4_10 = spikeTrap(138,117)
spk5_10 = spikeTrap(140,117)
spk6_10 = spikeTrap(142,117)
spk7_10 = spikeTrap(144,117)
spk8_10 = spikeTrap(146,117)
spk9_10 = spikeTrap(132,118)
spk10_10 = spikeTrap(134,118)
spk11_10 = spikeTrap(136,118)
spk12_10 = spikeTrap(138,118)
spk13_10 = spikeTrap(140,118)
spk14_10 = spikeTrap(142,118)
spk15_10 = spikeTrap(144,118)
spk16_10 = spikeTrap(146,118)

room10spikes = [spk1_10,spk2_10,spk3_10,spk4_10,spk5_10,spk6_10,spk7_10,spk8_10,
                spk9_10,spk10_10,spk11_10,spk12_10,spk13_10,spk14_10,spk15_10,spk16_10]

spk1_11 = spikeTrap(129,95)
spk2_11 = spikeTrap(129,96)
spk3_11 = spikeTrap(129,97)
spk4_11 = spikeTrap(129,98)
spk5_11 = spikeTrap(133,95)
spk6_11 = spikeTrap(133,96)
spk7_11 = spikeTrap(133,97)
spk8_11 = spikeTrap(133,98)
spk9_11 = spikeTrap(143,95)
spk10_11 = spikeTrap(143,96)
spk11_11 = spikeTrap(143,97)
spk12_11 = spikeTrap(143,98)
spk13_11 = spikeTrap(147,95)
spk14_11 = spikeTrap(147,96)
spk15_11 = spikeTrap(147,97)
spk16_11 = spikeTrap(147,98)
spk17_11 = spikeTrap(131,95)
spk18_11 = spikeTrap(131,98)
spk19_11 = spikeTrap(145,95)
spk20_11 = spikeTrap(145,98)

room11spikes = [spk1_11,spk2_11,spk3_11,spk4_11,spk5_11,spk6_11,spk7_11,spk8_11,spk9_11,spk10_11,
                spk11_11,spk12_11,spk13_11,spk14_11,spk15_11,spk16_11,spk17_11,spk18_11,spk19_11,spk20_11]

#---- FIRE TRAPS ----#
# NAME: fire + roomID_TrapID

fire1_5 = wallTrap(32,126,'d')

fire1_6 = wallTrap(44,98,'r')
fire2_6 = wallTrap(44,101,'r')

room6fire = [fire1_6, fire2_6]

fire1_7 = wallTrap(16,100,'r')
fire2_7 = wallTrap(16,96,'r')
fire3_7 = wallTrap(2,98,'l')
fire4_7 = wallTrap(2,94,'l')

room7fire = [fire1_7,fire2_7,fire3_7,fire4_7]

fire1_8 = wallTrap(14,75,'r')
fire2_8 = wallTrap(2,70,'l')
fire3_8 = wallTrap(2,67,'l')

room8fire = [fire1_8,fire2_8,fire3_8]

fire1_9 = wallTrap(99,117,'u')
fire2_9 = wallTrap(111,117,'u')

room9fire = [fire1_9,fire2_9]

boss = item.boss.Boss(67, 139) 

#hart = Colectable(67,140)