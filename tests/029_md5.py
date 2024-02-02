import hashlib

fname = '001.txt'

def hashfile(afile, hasher, blocksize=65536):
	buf = afile.read(blocksize)
	while len(buf) > 0:
		hasher.update(buf)
		buf = afile.read(blocksize)
	return hasher.hexdigest()

def main():
	#hasher = hashlib.sha256()
	hasher = hashlib.md5()
	ret = hashfile(open(fname, 'rb'), hasher)
	print(ret)


if __name__ == "__main__":
	main()
