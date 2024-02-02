def checkio(data):
	data.sort()
	sz = len(data)
	ind = sz // 2
	if sz % 2 == 1:
		return data[ind]
	else:
		return (data[ind - 1] + data[ind]) / 2

if __name__ == "__main__":
	print(checkio([1, 2, 3, 4, 5]) == 3)
	print(checkio([3, 1, 2, 5, 3]) == 3)
	print(checkio([1, 300, 2, 200, 1]) == 2)
	print(checkio([3, 6, 20, 99, 10, 15]) == 12.5)
	print(checkio(list(range(1000000))) == 499999.5)
