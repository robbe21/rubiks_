from sty import fg, bg, ef, rs, RgbFg, Style, RgbBg
	


def set_colours(cube):

	# bg.orange = Style(RgbBg(255, 150, 50))
	# fg.orange = Style(RgbFg(255, 150, 50))

	for face in cube.U.face:
		x = ""
		for i in range(3):
			if (len(str(face[i])) < 2):
				x = " "
			face[i] = fg.white + bg.white + face[i] + x + bg.rs + fg.rs

	for face in cube.L.face:
		x = ""
		for i in range(3):
			if (len(str(face[i])) < 2):
				x = " "
			face[i] = fg.orange + bg.orange + face[i] + x + bg.rs + fg.rs

	for face in cube.F.face:
		x = ""
		for i in range(3):
			if (len(str(face[i])) < 2):
				x = " "
			face[i] = fg.green + bg.green + face[i] + x + bg.rs + fg.rs

	for face in cube.D.face:
		x = ""
		for i in range(3):
			if (len(str(face[i])) < 2):
				x = " "
			face[i] = fg.yellow + bg.yellow + face[i] + x + bg.rs + fg.rs

	for face in cube.R.face:
		x = ""
		for i in range(3):
			if (len(str(face[i])) < 2):
				x = " "
			face[i] = fg.red + bg.red + face[i] + x + bg.rs  + fg.rs

	for face in cube.B.face:
		x = ""
		for i in range(3):
			if (len(str(face[i])) < 2):
				x = " "
			face[i] = fg.blue + bg.blue + face[i] + x + bg.rs + fg.rs
	



