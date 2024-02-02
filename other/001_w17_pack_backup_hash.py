import hashlib
import os
import shutil
import sys


file_name = 'w17_07'
#res_file_name = '_hashes'
#flash_drive = 'G:\\'
flash_drive = 'N:\\w\\_tmp\\flash\\'
flash_drive_dummy = 'zzzflash'


def hashfile(afile, hasher, blocksize=65536):
	buf = afile.read(blocksize)
	while len(buf) > 0:
		hasher.update(buf)
		buf = afile.read(blocksize)
	return hasher.hexdigest()


def calc_hash():
	#hasher = hashlib.sha256()
	hasher = hashlib.md5()
	hash_str = hashfile(open(file_name, 'rb'), hasher)

	#with open (res_file_name, "w") as out:
	#	out.write(hash_str + " " + file_name + "\n")

	return hash_str


def check_hash_str(hash_str):

	ok = False
	cur_hash = ''

	try:
		with open ('w17_07.md5', "r") as f:
			content = f.readlines()
			cur_hash = content[0].strip().split()[0]
			if cur_hash == hash_str:
				ok = True
	except:
		pass

	if ok:
		sys.stdout.write("All OK, hash is %s\n" % cur_hash)
	else:
		sys.stdout.write("!!!problem with hash. current is %s, needed %s\n" % (cur_hash, hash_str))


def delete_unneeded_files():
	try:
		os.remove('w17_07.md5')
	except:
		pass


def move_delete_backups():
	try:
		shutil.rmtree('prev.bak01.bak')
		os.rename('prev.bak', 'prev.bak01.bak')
		os.renames('_hashes', 'prev.bak/_hashes')
		os.renames('w17_07', 'prev.bak/w17_07')
		os.renames('w17_07.md5', 'prev.bak/w17_07.md5')
	except:
		pass


def check_flash_drive_dummy():
	if not os.path.isfile(os.path.join(flash_drive, flash_drive_dummy)):
		sys.stdout.write("!!!flash_drive_dummy not exist\n")
		sys.exit()


def get_flash_folder():
	ret = ''

	for dirpath, dirnames, filenames in os.walk(flash_drive):
		list2 = [x for x in dirnames if x[:6] == 'w17_v_']
		for d in list2:
			if not ret or ret < d:
				ret = d;

	sys.stdout.write(ret)
	sys.stdout.write("\n")
	return ret


def copy_from_flash_drive():
	check_flash_drive_dummy()
	flash_folder = os.path.join(flash_drive, get_flash_folder())
	shutil.copyfile(os.path.join(flash_folder, 'w17_07'), 'w17_07')
	shutil.copy(os.path.join(flash_folder, 'w17_07.md5'), 'w17_07.md5')
	

if __name__ == "__main__":
	check_flash_drive_dummy()

	move_delete_backups()
	copy_from_flash_drive()

	hash_str = calc_hash()
	check_hash_str(hash_str)
