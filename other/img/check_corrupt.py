
import getopt
import fnmatch
#import re
import os
import os.path
import sys
import subprocess

g_bad = False

def is_image(file_name):
	ext = os.path.splitext(file_name)[-1].lower()
	if ext == '.jpg' or ext == '.jpeg' or ext == '.jpg':
		return True
	else:
		if ext != '.sh':
			print("!!!File %s unknown format!" % file_name)
	return False


def is_corrupt(file_name):
	cmd_line = ['jpeginfo', '--check', file_name]

	try:
		ret = subprocess.check_output(cmd_line, stderr=subprocess.STDOUT)
	except:
		ret = b'Error'

	return ret


def check_files(files):
	global g_bad

	for f in files:
		if is_image(f):
			status = is_corrupt(f).decode('utf-8').rstrip('\n')
			#print(status[-4:])
			if status[-4:] != '[OK]':
				g_bad = True
				print("!!!!ERROR!!!! %s: %s" % (f, status))

def main():
	pathname = "./"
	for dirpath, dirnames, filenames in os.walk(pathname):
		check_files(os.path.join(dirpath, f) for f in filenames)

	if not g_bad:
		print("All OK")
	else:
		print("!!!Errors!!!")


if __name__ == "__main__":
	main()
