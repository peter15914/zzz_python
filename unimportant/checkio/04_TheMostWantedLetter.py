from collections import Counter

def checkio_0(data):
	data = data.lower()
	freq = {}

	for c in data:
		freq[c] = 0

	d = data[0]

	max_val = 0
	for c in data:
		if c.isalpha():
			freq[c] = freq[c]  + 1
			if freq[c] > max_val:
				max_val = freq[c]
				d = c

	for c in data:
		if (freq[c] == max_val) and (c < d):
			d = c

	return d

def checkio(data):
	c = Counter([x for x in data.lower() if x.isalpha()])
	_max = c.most_common()[0][1]

	d = 'z'
	for x in list(c):
		if (c[x] == _max) and (x < d):
			d = x

	return d


#if False:
if __name__ == "__main__":
	print(checkio("Hello World!") == "l")
	print(checkio("How do you do?") == "o")
	print(checkio("One") == "e")
	print(checkio("Oops!") == "o")
	print(checkio("AAaooo!!!!") == "a")
	print(checkio("abe") == "a")

#if True:
if False:
	checkio("Hello World!")
	checkio("How do you do?")
	checkio("One")
	checkio("Oops!")
	checkio("AAaooo!!!!")
	checkio("abe")
