#work_dir = 'H:/zm/zwriter_wrk/__res/__cur_wrk/'
work_dir = 'H:/zm/zwriter_wrk/__res_kwd/'

f2 = open(work_dir + '____concat', 'w')

a = set()

def processFile (name):
	global a
	fullname = work_dir + name
	f = open(fullname, 'r')
	for line in f:
		f2.write(line)
		#f2.write("\n")



processFile ('_all04.txt_left039_')
processFile ('res2012-12-06-01h06m00s765.txt')
processFile ('res2012-12-06-01h14m33s781.txt')
processFile ('res2012-12-06-01h18m54s968.txt')
processFile ('res2012-12-06-01h23m14s953.txt')
processFile ('res2012-12-06-01h27m33s484.txt')
