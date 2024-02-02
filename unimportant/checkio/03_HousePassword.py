def checkio(data):
	if len(data) < 10:
		return False
	b1 = False
	b2 = False
	b3 = False
	for c in data:
		if c.isdigit():
			b1 = True
		elif c.isupper():
			b2 = True
		elif c.islower():
			b3 = True
	return b1 and b2 and b3
	

if __name__ == "__main__":
	print(checkio('A1213pokl') == False)
	print(checkio('bAse730onE') == True)
	print(checkio('asasasasasasasaas') == False)
	print(checkio('QWERTYqwerty') == False)
	print(checkio('123456123456') == False)
	print(checkio('QwErTy911poqqqq') == True)
