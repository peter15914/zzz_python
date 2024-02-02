import utils

g_file_name = r'tmp2.avi'

def calc_hash2file(file_name, res_file_name):

	hash_str = utils.calc_hash(file_name)

	if res_file_name:
		with open (res_file_name, "w") as out:
			out.write(hash_str + " " + file_name + "\n")

if __name__ == "__main__":
	calc_hash2file(g_file_name, g_file_name+'.md5');
