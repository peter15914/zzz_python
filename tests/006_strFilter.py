f = open('Z:/_docs/various/nevosoft/002.txt', 'r')
f2 = open('Z:/_docs/various/nevosoft/002_res.txt', 'w')

a = set()

for line in f:
	if not line in a:
		f2.write(line);
		a = a | set([line]);
