import subprocess

file_name = '130630.avi'

with open(file_name + ".hash","wb") as out:
	subprocess.call(['md5deep.exe', '-e', file_name], stdout=out)
