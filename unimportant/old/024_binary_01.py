import time

chunksize = 2 ** 20

g_file_name = r'N:\w\tmp_binary\tmp\123\001'
g_out_file_name = r'N:\w\tmp_binary\tmp\123\001_2'

#g_file_name = r'N:\w\tmp_binary\tmp\_res_001'
#g_out_file_name = r'N:\w\tmp_binary\tmp\_res_002'

g_xor_base = 0x01
#g_pack = True
g_pack = False
g_pass = 'abc'

g_chunk2 = bytearray(chunksize)

def process_file(file_name, out_file_name):
	f = open(file_name, "rb")
	if not f: return

	f2 = open(out_file_name, "wb")
	if not f2: return

	while True:
		chunk = f.read(chunksize)
		if not chunk: break
		chunk2 = process_chunk(chunk)
		f2.write(chunk2)

def process_chunk(chunk):
	return process_chunk_xor(chunk)
	#return process_chunk_xor_pass_prev(chunk)

def process_chunk_xor(chunk):
	chunk2 = bytearray()
	for b in chunk:
		#b = b ^ g_xor_base
		chunk2.append(b)
	return chunk2

def process_chunk_xor_pass_prev(chunk):
	chunk2 = bytearray()

	prev = 0
	pass_len = len(g_pass)
	pass_ind = 0
	cnt = 0

	for b in chunk:
		tmp_prev = b

		b = b ^ g_xor_base
		cc = ord(g_pass[pass_ind])
		assert cc >= 0 and cc < 256
		b = b ^ cc
		b = b ^ prev

		pass_ind = pass_ind + 1
		if pass_ind >= pass_len:
			pass_ind = 0

		cnt = (cnt + 1) % 256

		if g_pack:
			prev = tmp_prev
		else:
			prev = b

		chunk2.append(b)
	return chunk2

if __name__ == "__main__":
	start_time = time.clock()

	print("chunk is", chunksize)
	process_file(g_file_name, g_out_file_name)

	print('total time:', time.clock() - start_time)
