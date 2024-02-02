
def process():
	fname = r'R:\_docs\zm\various\_007\_tmp\222'
	res_fname = fname + 'res'

	with open (res_fname, "w") as out:
		with open (fname, "r") as f:
			for line in f:
				line = line.rstrip()
				jj = line.find('see declaration')
				if jj != -1:
					jj = line.find('::', jj)
					s = line[jj+2:]
					out.write(s + "\n")

if __name__ == "__main__":
	process()
