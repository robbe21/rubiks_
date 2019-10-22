
from sty import fg, bg, ef, rs, RgbFg, Style, RgbBg


class Face:
	def __init__(self, name, face, fgcolor, bgcolor):
		self.name = name
		self.face = face
		self.bgcolor = bgcolor
		self.fgcolor = fgcolor


	# def set_colour(self):
	# 	# print(self.name)
	# 	for arrays in self.face:
	# 		for array in arrays:
	# 			for char in array:
	# 				char = self.fgcolor + self.bgcolor + char + bg.rs + fg.rs



	def checkifsolved(self):
		faceletter = self.name[:1]
		faceletter = self.fgcolor + self.bgcolor + faceletter + " " + bg.rs + fg.rs
		for array in self.face:
			for char in array:
				if faceletter != char:
					return 0
		return 1

class Cube:
	def __init__(self, B, F, R, L, U, D):
		self.B = B
		self.F = F
		self.R = R
		self.L = L
		self.U = U
		self.D = D

	def	checkifsolved(self):
		if not B.checkifsolved() or not D.checkifsolved() or not U.checkifsolved() or not F.checkifsolved() or not L.checkifsolved() or not R.checkifsolved():
			return 0
		return 1
	# def set_colours(self):
	# 	self.B.set_colour()
	# 	self.F.set_colour()
	# 	self.R.set_colour()
	# 	self.L.set_colour()
	# 	self.U.set_colour()
	# 	self.D.set_colour()

bg.orange = Style(RgbBg(255, 150, 50))
fg.orange = Style(RgbFg(255, 150, 50))

#start make faces
B = Face("Back face", [['B', 'B', 'B'], ['B','B','B'], ['B','B','B']], fg.blue, bg.blue)
F = Face("Front face", [['F', 'F', 'F'], ['F','F','F'], ['F','F','F']], fg.green, bg.green)
R = Face("Right face", [['R', 'R', 'R'], ['R','R','R'], ['R','R','R']], fg.red, bg.red)
L = Face("Left face", [['L', 'L', 'L'], ['L','L','L'], ['L','L','L']], fg.orange, bg.orange)
U =	Face("Up face", [['U', 'U', 'U'], ['U','U','U'], ['U','U','U']], fg.white, bg.white)
D = Face("Down face", [['D', 'D', 'D'], ['D','D','D'], ['D','D','D']], fg.yellow, bg.yellow)


# set_colours(cube)

#end make faces
