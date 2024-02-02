import subprocess
import os
import sys

jpeg_quality = 80


def convert_file(dirpath, filename):
	print(filename)

	if not filename.lower().endswith(('.jpg','.jpeg')):
		return

	filenamepath = os.path.join(dirpath, filename)
	subprocess.call([r'C:\Progs\IrfanView\i_view32.exe', '' + filenamepath + '', '/resize=(1920,1080)',
						'/aspectratio', '/resample', '/jpgq='+str(jpeg_quality), '/convert=$D$N.jpg'])


if __name__ == "__main__":
	pathname = os.getcwd()
	for dirpath, dirnames, filenames in os.walk(pathname):
		for f in filenames:
			#print(d)
			convert_file(dirpath, f)
