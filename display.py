
def print_cube(cube):
	print()

	print("\t  " + " ".join(cube.U.face[0]) + "\n")
	print("\t  " + " ".join(cube.U.face[1]) + "\n")
	print("\t  " + " ".join(cube.U.face[2]) + "\n")

	print(" ".join(cube.L.face[0]) + "  " + " ".join(cube.F.face[0]) + "  " + " ".join(cube.R.face[0]) + "  " + " ".join(cube.B.face[0]) + "\n")
	print(" ".join(cube.L.face[1]) + "  " + " ".join(cube.F.face[1]) + "  " + " ".join(cube.R.face[1]) + "  " + " ".join(cube.B.face[1]) + "\n")
	print(" ".join(cube.L.face[2]) + "  " + " ".join(cube.F.face[2]) + "  " + " ".join(cube.R.face[2]) + "  " + " ".join(cube.B.face[2]) + "\n")

	print("\t  " + " ".join(cube.D.face[0]) + "\n")
	print("\t  " + " ".join(cube.D.face[1]) + "\n")
	print("\t  " + " ".join(cube.D.face[2]) + "\n")


