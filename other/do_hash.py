import hashlib
import os
import shutil


file_name = 'w17_07'
res_file_name = '_hashes'


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

	with open (res_file_name, "w") as out:
		out.write(hash_str + " " + file_name + "\n")


if __name__ == "__main__":
	calc_hash()
