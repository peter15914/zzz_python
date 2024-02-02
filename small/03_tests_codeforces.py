

def test01():
	x = 2 * 10 ** 9
	i = 1
	while int(x) > 0:
		print("%02d. %d" % (i, x))
		i += 1
		x /= 2

def test02_20C():
	n = 10000
	m = n-1
	w = 1000000
	print("%d %d" % (n, m))
	for i in range(0, m):
		print("%d %d %d" % (i+1, i+2, w))
		

if __name__ == "__main__":
	test02_20C()
