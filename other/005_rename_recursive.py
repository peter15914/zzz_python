import subprocess
import os
import sys

jpeg_quality = 80


def convert_file(dirpath, filename):
	#print(filename)

	if not filename.lower().endswith(('.jpg','.jpeg')):
		return

	need_prefix = os.path.basename(dirpath) + "-"
	if filename.startswith(need_prefix):
		return

	filenamepath = os.path.join(dirpath, filename)
	filenamepath2 = os.path.join(dirpath, need_prefix + filename)
	try:
		os.rename(filenamepath, filenamepath2)
	except:
		pass


if __name__ == "__main__":
	pathname = os.getcwd()
	for dirpath, dirnames, filenames in os.walk(pathname):
		for f in filenames:
			#print(d)
			convert_file(dirpath, f)
