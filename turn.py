def	turn_face(face):
	temp_char = face[2][0]
	face[2][0] = face[0][0]
	temp_char2 = face[2][2]
	face[2][2] = temp_char
	temp_char = face[0][2] 
	face[0][2] = temp_char2
	face[0][0] = temp_char

	temp_char = face[1][0]
	face[1][0] = face[0][1]
	temp_char2 = face[2][1]
	face[2][1] = temp_char
	temp_char = face[1][2]
	face[1][2] = temp_char2
	face[0][1] = temp_char

## turn top to the right

def turn_u_rev(cube):

	temp_R_face = cube.R.face.copy()
	temp_F_face = cube.F.face.copy()
	temp_B_face = cube.B.face.copy()

	cube.F.face[0] = cube.L.face[0]
	cube.R.face[0] = temp_F_face[0]
	cube.B.face[0] = temp_R_face[0]
	cube.L.face[0] = temp_B_face[0]

	
	turn_face(cube.U.face)

def turn_r(cube):
	
	temp1 = cube.F.face[0][2]
	temp2 = cube.F.face[1][2]
	temp3 = cube.F.face[2][2]

	cube.F.face[0][2] = cube.D.face[0][2]
	cube.F.face[1][2] = cube.D.face[1][2]
	cube.F.face[2][2] = cube.D.face[2][2]

	temp4 = cube.U.face[0][2]
	temp5 = cube.U.face[1][2]
	temp6 = cube.U.face[2][2]

	cube.U.face[2][2] = temp3
	cube.U.face[1][2] = temp2
	cube.U.face[0][2] = temp1

	temp1 = cube.B.face[0][0]
	temp2 = cube.B.face[1][0]
	temp3 = cube.B.face[2][0]

	cube.B.face[2][0] = temp4
	cube.B.face[1][0] = temp5
	cube.B.face[0][0] = temp6

	cube.D.face[0][2] = temp3
	cube.D.face[1][2] = temp2
	cube.D.face[2][2] = temp1

	for i in range(3):
		turn_face(cube.R.face)
	
def	turn_f(cube):

	temp1 = cube.R.face[0][0]
	temp2 = cube.R.face[1][0]
	temp3 = cube.R.face[2][0]

	cube.R.face[0][0] = cube.U.face[2][0]
	cube.R.face[1][0] = cube.U.face[2][1]
	cube.R.face[2][0] = cube.U.face[2][2]

	temp4 = cube.D.face[0][0]
	temp5 = cube.D.face[0][1]
	temp6 = cube.D.face[0][2]

	cube.D.face[0][2] = temp1
	cube.D.face[0][1] = temp2
	cube.D.face[0][0] = temp3

	temp1 = cube.L.face[0][2]
	temp2 = cube.L.face[1][2]
	temp3 = cube.L.face[2][2]

	cube.L.face[0][2] = temp4
	cube.L.face[1][2] = temp5
	cube.L.face[2][2] = temp6

	cube.U.face[2][2] = temp1
	cube.U.face[2][1] = temp2
	cube.U.face[2][0] = temp3
	for i in range(3):
		turn_face(cube.F.face)

def	turn_d(cube):

	temp1 = cube.R.face[2][0]
	temp2 = cube.R.face[2][1]
	temp3 = cube.R.face[2][2]

	cube.R.face[2][0] = cube.F.face[2][0]
	cube.R.face[2][1] = cube.F.face[2][1]
	cube.R.face[2][2] = cube.F.face[2][2]

	temp4 = cube.B.face[2][0]
	temp5 = cube.B.face[2][1]
	temp6 = cube.B.face[2][2]

	cube.B.face[2][0] = temp1
	cube.B.face[2][1] = temp2
	cube.B.face[2][2] = temp3

	temp1 = cube.L.face[2][0]
	temp2 = cube.L.face[2][1]
	temp3 = cube.L.face[2][2]

	cube.F.face[2][0] = temp1
	cube.F.face[2][1] = temp2
	cube.F.face[2][2] = temp3

	cube.L.face[2][0] = temp4
	cube.L.face[2][1] = temp5
	cube.L.face[2][2] = temp6

	for i in range(3):
		turn_face(cube.D.face)


def	turn_l(cube):
	temp1 = cube.F.face[0][0]
	temp2 = cube.F.face[1][0]
	temp3 = cube.F.face[2][0]

	cube.F.face[0][0] = cube.U.face[0][0]
	cube.F.face[1][0] = cube.U.face[1][0]
	cube.F.face[2][0] = cube.U.face[2][0]

	temp4 = cube.D.face[0][0]
	temp5 = cube.D.face[1][0]
	temp6 = cube.D.face[2][0]

	cube.D.face[2][0] = temp3
	cube.D.face[1][0] = temp2
	cube.D.face[0][0] = temp1

	temp1 = cube.B.face[0][2]
	temp2 = cube.B.face[1][2]
	temp3 = cube.B.face[2][2]

	cube.B.face[2][2] = temp4
	cube.B.face[1][2] = temp5
	cube.B.face[0][2] = temp6

	cube.U.face[0][0] = temp3
	cube.U.face[1][0] = temp2
	cube.U.face[2][0] = temp1

	for i in range(3):
		turn_face(cube.L.face)


def turn_u(cube):
	for i in range(3):
		turn_u_rev(cube)

def turn_b(cube):

	temp1 = cube.U.face[0][0]
	temp2 = cube.U.face[0][1]
	temp3 = cube.U.face[0][2]

	cube.U.face[0][0] = cube.R.face[0][2]
	cube.U.face[0][1] = cube.R.face[1][2]
	cube.U.face[0][2] = cube.R.face[2][2]

	temp4 = cube.L.face[0][0]
	temp5 = cube.L.face[1][0]
	temp6 = cube.L.face[2][0]

	cube.L.face[2][0] = temp1
	cube.L.face[1][0] = temp2
	cube.L.face[0][0] = temp3

	temp1 = cube.D.face[2][0]
	temp2 = cube.D.face[2][1]
	temp3 = cube.D.face[2][2]

	cube.R.face[2][2] = temp1
	cube.R.face[1][2] = temp2
	cube.R.face[0][2] = temp3

	cube.D.face[2][0] = temp4
	cube.D.face[2][1] = temp5
	cube.D.face[2][2] = temp6

	for i in range(3):
		turn_face(cube.B.face)




def do_move(move, cube):

	if (move == 'U'):
		turn_u(cube)
	elif (move == "U'"):
		for i in range(3):
			turn_u(cube)
	elif (move == "U2"):
		for i in range(2):
			turn_u(cube)
	elif (move == 'R'):
		turn_r(cube)
	elif (move == "R'"):
		for i in range(3):
			turn_r(cube)
	elif (move == "R2"):
		for i in range(2):
			turn_r(cube)
	elif (move == 'B'):
		turn_b(cube)
	elif (move == "B'"):
		for i in range(3):
			turn_b(cube)
	elif (move == "B2"):
		for i in range(2):
			turn_b(cube)
	elif (move == 'L'):
		turn_l(cube)
	elif (move == "L'"):
		for i in range(3):
			turn_l(cube)
	elif (move == "L2"):
		for i in range(2):
			turn_l(cube)
	elif (move == 'D'):
		turn_d(cube)
	elif (move == "D'"):
		for i in range(3):
			turn_d(cube)
	elif (move == "D2"):
		for i in range(2):
			turn_d(cube)
	elif (move == 'F'):
		turn_f(cube)
	elif (move == "F'"):
		for i in range(3):
			turn_f(cube)
	elif (move == "F2"):
		for i in range(2):
			turn_f(cube)