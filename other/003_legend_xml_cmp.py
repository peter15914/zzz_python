import xml.etree.ElementTree
import sys

bLegendShadingtypes = True


def add_to_map(dd, skey, sval):
	if skey in dd:
		if dd[skey] != sval:
			print("!!!Error, two different values for %s" % skey)
	else:
		dd[skey] = sval
		#print("%s -> %s" % (skey, sval))


def check_on_map(dd, skey, sval):
	if not (skey in dd):
		print("!!!Error, value was deleted for %s" % skey)
	else:
		if dd[skey] != sval:
			print("!!!Error, value was changed for %s, %s -> %s" % (skey, sval, dd[skey]))


def process_file1(dd, file_name, create_map):
	e = xml.etree.ElementTree.parse(file_name).getroot()

	for atype in e.findall('Item'):
		skey = atype.get('Id')#.lower()
		sval = atype.text#.lower()

		if create_map:
			add_to_map(dd, skey, sval)
		else:
			check_on_map(dd, skey, sval)


def process_file2(dd, file_name, create_map):
	e = xml.etree.ElementTree.parse(file_name).getroot()
	b = e[0][0]
	#print(b)

	for atype in b.findall('Domain'):
		#print(atype)
		skey = atype[0][0].text
		sval = ""

		if create_map:
			add_to_map(dd, skey, sval)
		else:
			check_on_map(dd, skey, sval)


def check_files(fname_new, fname_orig):
	dd = dict()

	if not bLegendShadingtypes:
		process_file1(dd, fname_new, True)
		process_file1(dd, fname_orig, False)
	else:
		process_file2(dd, fname_new, True)
		process_file2(dd, fname_orig, False)


if __name__ == "__main__":
	#redirect stdout to file
	sys.stdout = open('log.txt', 'w')

	#fname_new = r'N:\w\wbin\xml\legend.xml'
	fname_new = r'F:\work\various\_tmp\123\legendShadingtypes.xml'
	#fname_orig = r'N:\w\wbin\xml\legend_old.xml'
	#check_files(fname_new, fname_orig):

	with open(r'N:\w\wbin\xml\list2') as f:
	    for fname_orig in f.read().splitlines():
	    	if fname_orig:
		    	print(fname_orig)
		    	check_files(fname_new, fname_orig)

	print('End')
