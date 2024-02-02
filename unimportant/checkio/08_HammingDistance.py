
def checkio_0(x, y):
	t = x ^ y

	ret = 0
	while t > 0:
		ret = ret + t % 2
		t = t // 2

	return ret


checkio_1 = lambda n, m: format(n ^ m, 'b').count('1')


def checkio(n, m):
    return bin(n ^ m).count('1')


if __name__ == "__main__":
	print(checkio(117, 17) == 3)
	print(checkio(1, 2) == 2)
	print(checkio(16, 15) == 5)
