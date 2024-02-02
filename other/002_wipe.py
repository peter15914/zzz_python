import random


import time
import os
import uuid


chunksize = 0
chunks_in_file = 0


filescnt = 0
chunk = bytearray()


def gen_chunk():
	global chunk, chunksize

	chunk = bytearray(chunksize)

	for i in range(0, chunksize):
		chunk[i] = random.randint(0, 255)
	#cc = 0
	#for i in range(0, filesize):
	#	chunk[i] = cc
	#	cc = cc + 1
	#	if cc > 255:
	#		cc = 0


def wipe_file(filename):
	global filescnt

	f2 = open(filename, "wb")
	if not f2: return

	for i in range(0, chunks_in_file):
		f2.write(chunk)
	f2.close()

	filescnt += 1


def gen_file_in_folder(foldername):
	full_unique_name = os.path.join(foldername, 'z'+str(uuid.uuid4()))
	wipe_file(full_unique_name)
	

def wipe_folder(foldername, depth):

	if depth == 0:
		for i in range(0, 16):
			gen_file_in_folder(foldername)
	else:
		for i in range(0, 8):
			full_unique_name = os.path.join(foldername, 'z'+str(uuid.uuid4()))
			os.mkdir(full_unique_name)
			wipe_folder(full_unique_name, depth-1)

def large_files_wipe(folder_path):

	global chunksize, chunks_in_file

	#clastersize = 4096
	#filesize = clastersize * 256
	#filesize = clastersize

	chunksize = 1 * 1024 * 1024
	chunks_in_file = 1024

	gen_chunk()

	try:
		for i in range(0, 7):
			gen_file_in_folder(folder_path)
	except Exception as e: 
		print("!!!Error")
		print(e)
		traceback.print_exc()

def small_files_wipe(folder_path):

	global chunksize, chunks_in_file

	chunksize = 600
	chunks_in_file = 1

	gen_chunk()

	try:
		wipe_folder(folder_path, 5)
	except Exception as e: 
		print("!!!Error")
		print(e)
		traceback.print_exc()


if __name__ == "__main__":
	start_time = time.clock()

	random.seed()

	#large_files_wipe(r'D:/006/')
	small_files_wipe(r'F:/__2delete/007/')

	print('total time:', time.clock() - start_time)
	print('files created:', filescnt)
