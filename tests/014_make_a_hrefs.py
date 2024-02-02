


def make_links(file_name):
	res_file = file_name + "_res.html"
	f_res = open(res_file, 'w')

	f1 = open(file_name, 'r')
	for line in f1:
		line = line.strip()
		line = "<a href=\"%s\">%s</a>\n<br/>" % (line, line);
		f_res.write(line)
	f1.close()
	f_res.close()



#------------------------------------------------------------------------------------------
def main():
	make_links(r"/media/xxx62/w/various/006.txt")

#------------------------------------------------------------------------------------------
main()
