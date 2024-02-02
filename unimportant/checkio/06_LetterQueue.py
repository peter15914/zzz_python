
def letter_queue_0(q):
	res = []
	for cmd in q:
		if cmd == "POP":
			if res:
				res.pop(0)
		else:
			c = cmd[-1]
			res.append(c)
	return "".join(res)

def letter_queue(q):
	res = []
	for cmd in q:
		if cmd == "POP":
			if res: res.pop(0)
		else: res.append(cmd[-1])
	return "".join(res)


if __name__ == "__main__":
	print(letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT")
	print(letter_queue(["POP", "POP"]) == "")
	print(letter_queue(["PUSH H", "PUSH I"]) == "HI")
	print(letter_queue([]) == "")
