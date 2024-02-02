import subprocess
import sys
sys.path.insert(0, '/media/xxx63/r/python')
import utils
#---

g_folder = "/media/zzz/DISK_K/_data/_nick's_music"
g_res_file = "/media/zzz/DISK_K/_data/_nick's_music/_fdupes_res.txt"

if __name__ == "__main__":
	b = utils.query_yes_no("DO YOU WANT TO DELETE DUPES?")
	with open(g_res_file, "wb") as out:
		if b:
			subprocess.call(['fdupes', '-r', '-d', '-N', g_folder], stdout=out)
		else:
			subprocess.call(['fdupes', '-r', g_folder], stdout=out)
