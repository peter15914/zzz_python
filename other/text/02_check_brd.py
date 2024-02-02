
src_file = "BRD_00_BRD.txt"
dst_file = "_BRD_00_BRD_res.txt"

def check_str(line):
	global f_res

	words = line.split('\t')
	if len(words) == 0:
		return

	x1 = float(words[4])
	x2 = float(words[5])
	x3 = float(words[6])
	x4 = float(words[7])
	#if x1 >= x2 or x3 >= x4:
	if x2-x1 < 10  or x4-x3 < 10:
		f_res.write("%f\t%f\t%f\t%f\n" % (x1, x2, x3, x4))


def main():
	global f_res

	f = open(src_file, 'r')
	f_res = open(dst_file, 'w')

	i = 0
	for line in f:
		if i > 0:
			new_str = check_str(line)
		i = i + 1


	f.close()
	f_res.close()


if __name__ == "__main__":
	main()
