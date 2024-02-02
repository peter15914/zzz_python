
folder = '/media/xxx62/w/various/030/'
res_folder = '/media/xxx62/w/various/030/zomb/'

src_file = folder + '002_zomb.txt'
f = open(src_file, 'r')

num = 0
name = ""
cnt = 0
gross = ""
for line in f:
	words = line.split('\t')
	if len(words) == 0:
		continue

	if line[0] == ';':
		continue

	b = True
	try:
		tt = int(words[0])
		num = tt
	except:
		b = False
	

	#line with title
	if b:
		name = words[1]

		#search for word with '$'
		for w in words:
			if w.find('$') != -1:
				gross = w
				break

	#print(words)
		
	lastw = words[-1].strip()
	if not lastw:
		lastw = words[-2].strip()

	#line with date date
	if lastw.find('/') != -1:
		year = lastw.strip()[-2:]

		line2 = "%s\t%s\t%s\n" % (name, lastw.strip(), gross)

		#print(name)
		#print(year)
		nyear = int(year)
		if nyear < 90 and nyear > 50:
			year = '80x'
		elif nyear >= 90 and nyear <= 94:
			year = '90-94'
		elif nyear >= 95 and nyear <= 99:
			year = '95-99'

		if nyear > 30 and nyear < 90:
			continue

		res_file = res_folder + year + '.txt'
		f_res = open(res_file, 'a')
		f_res.write(line2)
		cnt = cnt+1

		name = ""
		gross = ""
	#print(words)
	#if cnt == 4:
	#	break

print("cnt = ", cnt)

f_res.close()
