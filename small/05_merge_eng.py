
file_00_main = r"/media/xxx51/__razr_2esc/english_words.txt"
file_res = file_00_main + "_res.txt"
file_01 = r"/media/xxx51/__razr_2esc/111"

def process():
	cur_arr = []

	with open(file_00_main, "r") as f:
	    for word in f.read().splitlines():
	    	if word:
				cur_arr = cur_arr + [word]

	existed = set(cur_arr)

	new_arr = []
	
	with open(file_01, "r") as f:
	    for word in f.read().splitlines():
	    	if word and not word in existed:
				new_arr = new_arr + [word]
				existed.add(word)

	with open(file_res, "w") as out:
		for word in new_arr:
			out.write(word + "\n")
		for word in cur_arr:
			out.write(word + "\n")


if __name__ == "__main__":
	process()
	
