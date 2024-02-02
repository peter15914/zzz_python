#import subprocess
import os
#import sys

first = 15
files_count = 100
sz = 128

g_res_dir = "/media/xxx62/w/various/036_rand/"

def get_os_rand_bytes(sz):
	ret = os.urandom(sz)
	#with open("/dev/random", 'rb') as f:
	#	ret = f.read(sz)
	return ret

def get_rand():
	for i in range(first, first + files_count):
		fname = g_res_dir + "%03d" % i
		with open(fname, "wb") as out:
			rand = get_os_rand_bytes(sz)
			out.write(rand)


if __name__ == "__main__":
	get_rand()
