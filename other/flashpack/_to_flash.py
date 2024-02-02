import flashpack

flashpack.g_home = True
g_file_names = ['work11']

flashpack.flash_drive = '/media/zzz/2706-CB49/'
flashpack.hard_drive = '/home/zzz/work/'


if __name__ == "__main__":
	flashpack.main_to_flash(g_file_names);
