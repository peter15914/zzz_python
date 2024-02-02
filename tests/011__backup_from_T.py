import shutil;

def _copy_ex (src_file):
	fullname1 = 'T:/' + src_file
	fullname2 = 'N:/_from_T/' + src_file
	shutil.copytree(fullname1, fullname2)


_copy_ex('sites')
_copy_ex('SVN')
_copy_ex('content')
