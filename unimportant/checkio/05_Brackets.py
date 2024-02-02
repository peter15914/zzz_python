
def checkio(data):
	br = []
	for c in data:
		if c == '(' or c == '[' or c == '{':
			br.append(c)
		if c == ')' or c == ']' or c == '}':
			if not br: return False
			cc = br.pop()
			if c == ')' and cc != '(': return False
			if c == ']' and cc != '[': return False
			if c == '}' and cc != '{': return False
		
	return not br


if __name__ == "__main__":
	print(checkio("((5+3)*2+1)") == True)
	print(checkio("{[(3+1)+2]+}") == True)
	print(checkio("(3+{1-1)}") == False)
	print(checkio("[1+1]+(2*2)-{3/3}") == True)
	print(checkio("(({[(((1)-2)+3)-3]/3}-3)") == False)
	print(checkio("2+3") == True)
	print(checkio("((5+{3)*2}+1)") == False)
