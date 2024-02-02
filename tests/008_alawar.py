exit

f2 = open('Z:/_docs/various/alawar/_urls.txt', 'w')

a = set()

def precessFile (name):
	global a

	#f2.write(';-----------------------------------------')
	#f2.write(name)
	#f2.write("\n")

	f = open(name, 'r')
	for line in f:
		i = line.find('.exe"')
		if i != -1:
			j = line.find('href="http://www.alawar.ru/download/', 0, i)
			if j != -1:
				line2 = line[j+6:i+4]
				if not line2 in a:
					f2.write(line2)
					f2.write("\n")
					a = a | set([line2]);


precessFile ('Z:/_docs/various/alawar/begalki')
precessFile ('Z:/_docs/various/alawar/biznes')
precessFile ('Z:/_docs/various/alawar/golovolomki.txt')
precessFile ('Z:/_docs/various/alawar/poisk_predmetov')
precessFile ('Z:/_docs/various/alawar/shariki')
precessFile ('Z:/_docs/various/alawar/strelyalki')
precessFile ('Z:/_docs/various/alawar/new-games')
