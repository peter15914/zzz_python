exit

f2 = open(r"Q:\no_svn\other\4typing\004.txt", 'w')

def processFile():

	f = open(r"Q:\no_svn\other\4typing\003.txt", 'r')

	cnt = 0
	for line in f:
		line2 = line.rstrip()
		if not line2:
			continue

		f2.write(line2 + ' ')
		cnt += 1
		if cnt >= 20:
			cnt = 0;
			f2.write('\n')


processFile()
