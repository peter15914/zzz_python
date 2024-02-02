
src_file = 'Q:/w/afg/titles.txt'
res_file = 'Q:/w/afg/tmp_titles_urls.html'

f_res = open(res_file, 'w')

f1 = open(src_file, 'r')
cur_url = '';
game_mode = False

for line in f1:
	if not line.rstrip():
		continue;

	i1 = line.find('http://')
	if i1 != -1:		#url
		assert i1 == 0
		cur_url = line
		game_mode = False
	else:
		i2 = line.find('//')
		if i2 != -1:		#comment
			assert i2 == 0
		else:
			i3 = line.find('#game')
			if i3 != -1:		#game
				assert i3 == 0
				game_mode = True
			else:
				res_line = '<a href="%s">%s</a>\n' % (cur_url.rstrip(), line.rstrip());
				f_res.write(res_line)
				if game_mode:
					res_line = '<a href="%s">%s</a>\n' % (cur_url.rstrip(), line.rstrip() + " игра");
					f_res.write(res_line)
					res_line = '<a href="%s">%s</a>\n' % (cur_url.rstrip(), "игра " + line.rstrip());
					f_res.write(res_line)
					


		
f1.close()
f_res.close()

print('Ok!')
