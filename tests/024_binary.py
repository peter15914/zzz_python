import time

chunksize = 2 ** 20

#g_file_name = r'N:\w\tmp_binary\tmp\_res_001'
#g_out_file_name = r'N:\w\tmp_binary\tmp\_res_002'


g_xor_base = 0x61
g_pack = True
#g_pack = False
g_pass = 'xxx'

g_chunk2 = bytearray(chunksize)

def process_file(file_name, out_file_name):
	f = open(file_name, "rb")
	if not f: return

	f2 = open(out_file_name, "wb")
	if not f2: return

	while True:
		numread = f.readinto(g_chunk2)
		#print("numread = ", numread)
		#print("len(g_chunk2) = ", len(g_chunk2))
		if not numread: break
		process_chunk(numread)
		if numread == len(g_chunk2):
			f2.write(g_chunk2)
		else:
			chunk3 = g_chunk2[0:numread]
			f2.write(chunk3)


def process_chunk(numread):
	return process_chunk_xor(numread)
	#return process_chunk_xor_pass_prev(numread)


def process_chunk_xor(numread):
	_len = numread
	for i in range(0, _len):
		g_chunk2[i] = g_chunk2[i] ^ g_xor_base


def process_chunk_xor_pass_prev(numread):
	_len = numread

	prev = 0
	pass_len = len(g_pass)
	pass_ind = 0
	cnt = 0

	b = 0
	for i in range(0, _len):
		b = g_chunk2[i]
		tmp_prev = b

		cc = ord(g_pass[pass_ind])
		#assert cc >= 0 and cc < 256

		b = b ^ g_xor_base ^ cc ^ prev ^ cnt

		pass_ind = (pass_ind + 1) % pass_len
		cnt = (cnt + 1) % 256

		if g_pack:
			prev = tmp_prev
		else:
			prev = b

		g_chunk2[i] = b


if __name__ == "__main__":
	start_time = time.clock()

	print("chunk is", chunksize)

	#process_file(g_file_name, g_out_file_name)

"""	
	g_dir = '/media/xxx62/w/various/036_rand/shfl/'
	for i in range(13, 114):
		f_name = g_dir + "%03d" % i;
		f_name_res = g_dir + "res/%03d" % i;
		process_file(f_name, f_name_res)
		#process_file(f_name + "_res", f_name + "_res2")
"""

	print('total time:', time.clock() - start_time)
