import os
import time
import utils

chunksize = 2 ** 20

g_path = r'D:\zm\w17_pack\w17_data\123'

"""
g_file_names = [
	r'000',
	r'001'
]
"""

g_out_file_name = r'tmp.avi'


def get_file_names():
	#return g_file_names
	ret = []
	for i in range(1, 31):
		fname = "tmp.avi.%03d" % i
		ret += [fname]

	return ret


def process_files():
	f2 = open(os.path.join(g_path, g_out_file_name), "wb")
	if not f2: return

	file_names = get_file_names()

	for file_name in file_names:
		full_file_name = os.path.join(g_path, file_name)
		#print(full_file_name)

		f = open(full_file_name, "rb")
		if not f:
			assert False
			break
		while True:
			chunk = f.read(chunksize)
			if not chunk: break
			f2.write(chunk)

	f2.close()



if __name__ == "__main__":
	start_time = time.clock()
	process_files()
	print('total time:', time.clock() - start_time)
	print(utils.calc_hash(os.path.join(g_path, g_out_file_name)))
