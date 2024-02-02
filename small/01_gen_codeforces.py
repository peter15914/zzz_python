g_res_file = "/media/xxx61/r/eclipse2/ews02_codeforces/codef/input/Rnd600_A_7.txt"

def gen(out, nn):
	out.write(str(nn*2) + "\n")
	
	for i in range(0, nn):
		#out.write("433494437 701408733")
		out.write("4849845 94101027")
		out.write(" ")



def gen2(out, nn, dd):
	out.write(str(nn) + "\n")
	
	for i in range(0, nn):
		out.write(str(dd))
		out.write(" ")

def gen3(out, nn):
	out.write(str(nn) + "\n")
	
	for i in range(0, nn):
		out.write(str(i+1))
		out.write(" ")

def gen4(out, nn):
	out.write(str(nn) + "\n")
	
	cc = 1000000000
	for i in range(0, nn):
		out.write(str(cc))
		cc = cc - 2
		out.write(" ")

if __name__ == "__main__":
	with open(g_res_file, "w") as out:
		gen(out, 500)
		#gen2(out, 1000, 669278610)
		#gen3(out, 1000)
		#gen4(out, 1000)
