import os;

glob_folder = 'T:/sites/_kaz3/'

def create_site_fold(num):
	fold = glob_folder + 'z_kaz3_%03d' % num
	fold2 = fold + "/index_files"
	print('fold =  ' + fold + '; ' + 'fold2 =  ' + fold2)
	os.mkdir(fold2)

for i in range(21, 40):
	create_site_fold(i)
	
