
f2 = open('Z:/w/sapeUV/wrk/res5/_all_urls.txt', 'w')

a = set()

def processFile (name):
	global a
	fullname = 'Z:/w/sapeUV/wrk/res5/' + name
	f = open(fullname, 'r')
	for line in f:
		if(line.find('URL страницы') == -1):
			f2.write(line)
			#f2.write("\n")


processFile ('kaz_14_export_linksseo_20121125091707.xls')
processFile ('kaz_15_export_linksseo_20121125091734.xls')
processFile ('kaz_16_export_linksseo_20121125091822.xls')
processFile ('kaz_17_export_linksseo_20121125091833.xls')
processFile ('kaz_18_export_linksseo_20121125091800.xls')
processFile ('kaz_19_export_linksseo_20121125091812.xls')
processFile ('kaz_20_export_linksseo_20121125091844.xls')



