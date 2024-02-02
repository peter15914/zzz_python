#--при помощи этого скрипта в итоговый файл копируются только ссылки на галереи сразу из кучи файлов в один

res_fold = 'T:/sites/_db/_kaz3/_links_temp/'
glob_src_fold = 'T:/sites/_db/_kaz3/'

#------------------------------------------------------------------------------------------
def make_links(i):
	res_file = res_fold + 'z_kaz3_%03d.txt' % i
	f_res = open(res_file, 'w')

	src_fold = glob_src_fold + 'z_kaz3_%03d' % i + '/'
	src_file_1 = src_fold + 'sapa_links.txt'
	src_file_2 = src_fold + 'sapa_links2.txt'

	f1 = open(src_file_1, 'r')
	t = False
	for line in f1:
		if(line.find('/30/') != -1):
			t = True;
		if t:
			f_res.write(line)
	f1.close()

	f2 = open(src_file_2, 'r')
	t = False
	for line in f2:
		if(line.find('/30/') != -1):
			t = True;
		if t:
			f_res.write(line)
	f2.close()

	f_res.close()




#------------------------------------------------------------------------------------------
def main():
	for i in range(30, 51):
		make_links(i)

#------------------------------------------------------------------------------------------
main()
