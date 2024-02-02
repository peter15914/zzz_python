import os
import sys
sys.path.insert(0, 'xxx/r/python')
import utils

src_folder = 'xxx/aaa.ru/gfx'
dst_folder = 'xxx/tmp/sg'


def process(ind1, ind2, file_format):
	for i in range(ind1, ind2):
		
		file_name = file_format % i;
		#src_file_name = os.path.join(src_folder, file_name)
		src_file_name = 'xxx/gfx/blank.jpg'
		dst_file_name = os.path.join(dst_folder, file_name)
		
		try:
			os.makedirs(os.path.dirname(dst_file_name))
		except:
			pass
	
		utils.copyFile(src_file_name, dst_file_name)		
	


if __name__ == "__main__":
	process(1, 5, "_img/i%03d.jpg")
	process(1, 67, "big/%03d.jpg")
	process(1, 67, "small/%03d.jpg")
