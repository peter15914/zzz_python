
src_file = "338.txt"
dst_file = "338_res.txt"

def convert_str(line):
	res = ''

	cur_word_len = 0

	for c in line:
		if not c.isalpha():
			cur_word_len = 0
		else:
			if cur_word_len == 0:
				c = c.upper()
			cur_word_len = cur_word_len + 1
			if cur_word_len <= 7:
				res = res + c

	return 'Str_' + res


def main():
	f = open(src_file, 'r')
	f_res = open(dst_file, 'w')

	for line in f:
		new_str = convert_str(line)
		f_res.write(new_str + ";;;;;\n")


	f.close()
	f_res.close()


if __name__ == "__main__":
	main()
