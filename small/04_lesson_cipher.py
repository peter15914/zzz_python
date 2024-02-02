
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
code_word = "тюмень"
code = ""

def create_code():
	global code
	code = code_word
	#print(len(alphabet))

	s = set()
	for c in code: s.add(c)
	#print(s)

	for c in alphabet:
		if c not in s:
			s.add(c)
			code += c
	#print(code)
	#print(len(code))

def process_char(c):
	if c in [' ', ',', '.']:
		return c

	sz = len(alphabet)
	if (sz != len(code)):
		assert False
		return 'X'

	for i in range(0, sz):
		if alphabet[i] == c:
			return code[i]

	return 'X'
	
	
def process_str(s):
	ret = ""
	for c in s:
		ret += process_char(c)
	return ret



if __name__ == "__main__":
	create_code()

	print(alphabet)
	print(code)

	s = "спокойной ночи, малыши"
	print(s)
	s = process_str(s)
	print(s)
