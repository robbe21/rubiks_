#!/usr/bin/env python3

import sys
import os
from sty import fg, bg, ef, rs, RgbFg, Style, RgbBg
from colors import set_colours
from display import print_cube
from turn import * 
from cube import *


#make cube
cube = Cube(B, F, R, L, U, D)
##colour faces
set_colours(cube)


inpt = sys.argv
if len(inpt) < 2:
	exit("no moves - play as argument if you want to play with the cube")
moves = inpt[1].split()


##start lay with the cube
if (moves[0] == "play"):
	g = " "
	if len(inpt) > 2:
		moves = inpt[2].split()
		for move in moves:
			do_move(move, cube)
	while (1):
		os.system('clear')
		print_cube(cube)
		if cube.checkifsolved() and g == "check":
			print("cube is solved")
		elif g == "check":
			print("cube is not solved")
		g = input("Moves(\"Q\" to quit - \"check\" to check): ")
		print(g)
		if (g == 'Q' or g == 'q'):
			break
		do_move(g, cube)

##end play with the cube

#start do moves
for move in moves:
	do_move(move, cube)
#end do moves


os.system('clear')
print_cube(cube)
