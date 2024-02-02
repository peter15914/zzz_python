
src_file = 'T:/w/various/022/dirs.txt'
res_file = 'T:/w/various/022/result.txt'

f_res = open(res_file, 'w')
f1 = open(src_file, 'r')

#cd dirname
#i_view32.exe .\*.jpg /resize=(1280,1024) /resample /aspectratio /convert=.\*.jpg /jpgq=90
#cd ..

for line in f1:
	if not line.rstrip():
		continue;

	f_res.write("\n")

	res_line = 'cd %s\n' % (line.rstrip());
	f_res.write(res_line)
	f_res.write('i_view32.exe .\*.jpg /resize=(1280,1024) /resample /aspectratio /convert=.\*.jpg /jpgq=90\n')

	f_res.write("cd ..\n")

		
f1.close()
f_res.close()

print('Done!')
