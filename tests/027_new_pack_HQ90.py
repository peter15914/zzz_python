import subprocess
import os
import sys


def convert_dir(dirName):
	origWD = os.getcwd()
	#print(origWD)
	newDir = os.path.join(origWD, dirName)
	#print(newDir)

	os.chdir(newDir)
	subprocess.call([r'C:\Progs\IrfanView\i_view32.exe', '*.jpg', '/resize=(1920,1080)', '/aspectratio', '/resample', '/jpgq=90', '/convert=$D$N.jpg'])
	os.chdir(origWD)


if __name__ == "__main__":
	pathname = os.getcwd()
	for dirpath, dirnames, filenames in os.walk(pathname):
		for d in dirnames:
			#print(d)
			convert_dir(d)
