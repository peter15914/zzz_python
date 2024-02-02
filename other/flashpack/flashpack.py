import hashlib
import os
import shutil
import sys
import utils
import pyperclip


g_home = False
g_add_suffix = False
flash_drive = '?error*'
hard_drive = '?error*'
flash_drive_dummy = 'zzzflash'
hard_drive_dummy = 'zzzdrive'
log_file_name = 'flashpack.log'
g_log = None


def md5name(file_name):
    return file_name + '.md5';


def calc_hash2file(file_name, res_file_name):

    hash_str = utils.calc_hash(file_name)

    if res_file_name:
        with open (res_file_name, "w") as out:
            out.write(hash_str + " " + file_name + "\n")


def print_log(sstr):
    print(sstr)
    if not (g_log is None):
        g_log.write(sstr)


def check_hash_str(hash_str, md5_file_name_):

    ok = False
    cur_hash = ''

    try:
        with open (md5_file_name_, "r") as f:
            content = f.readlines()
            cur_hash = content[0].strip().split()[0]
            if cur_hash == hash_str:
                ok = True
    except:
        pass

    if ok:
        print_log("All OK, hash is %s\n" % cur_hash)
    else:
        print_log("!!!problem with hash. current is %s, needed %s\n" % (cur_hash, hash_str))

    return ok


#def delete_unneeded_files():
#    try:
#        os.remove(md5name(file_name))
#    except:
#        pass


def move_delete_backups(file_names):
    
    if g_home:
        return

    try:
        shutil.rmtree('prev.bak01.bak')
    except:
        pass

    try:
        os.rename('prev.bak', 'prev.bak01.bak')
    except:
        pass

    try:
        for file_name in file_names:
            os.renames(file_name, os.path.join('prev.bak', file_name))
            os.renames(md5name(file_name), os.path.join('prev.bak', md5name(file_name)))
    except:
        print_log("!!Can't move_delete_backups")
        pass


def check_drive_dummys():

    while True:
        if os.path.isfile(os.path.join(flash_drive, flash_drive_dummy)):
            break

        print_log("!!!flash_drive_dummy not exist\n")
        if not utils.query_yes_no('Retry?'):
            print_log("Abortion")
            sys.exit()

    while True:
        if os.path.isfile(os.path.join(hard_drive, hard_drive_dummy)):
            break

        print_log("!!!hard_drive_dummy not exist\n")
        if not utils.query_yes_no('Retry?'):
            print_log("Abortion")
            sys.exit()

def get_num_from_folder(folder):

    if folder[:6] != 'w18_v_':
        assert False
        return 0
    if folder[-5:] == '_2wrk':
        return int(folder[6:-5])
    return int(folder[6:])


def get_last_folder(path):
    ret = ''

    for dirpath, dirnames, filenames in os.walk(path):
        list2 = [x for x in dirnames if x[:6] == 'w18_v_']
        for d in list2:
            try:
                if not ret or get_num_from_folder(ret) < get_num_from_folder(d):
                    ret = d
            except:
                print_log("!!!bad folder: " + d)

    #print_log("get_last_folder: " + ret)
    return ret


def get_flash_folder():

    return get_last_folder(flash_drive)


def get_new_folder(path, add2wrk):

    ret = get_last_folder(path)
    if ret[-5:] == '_2wrk':
        ret = ret[:-5]

    #print_log(ret, '\n');

    num = 0
    try:
        num = int(ret[6:])
    except:
        #print_log("!Error get_new_folder")
        #assert False
        #sys.exit()
        num = 0

    ret = "w18_v_%03d" % (num + 1)
    if add2wrk:
        ret = ret + '_2wrk';
    return ret


def check_not_exist(file_name):
    if os.path.exists(file_name):
        print_log("!File already exists: " + file_name + "\n")
        if not utils.query_yes_no('Continue?'):
            print_log("Abortion")
            sys.exit()


def copy_from_flash_drive(flash_folder, file_names):
    check_drive_dummys()

    flash_path = os.path.join(flash_drive, flash_folder)

    if g_home:
        dst_path = os.path.join(hard_drive, flash_folder)
        if os.path.exists(dst_path):
            new_folder = get_new_folder(hard_drive, g_add_suffix)
            dst_path = os.path.join(hard_drive, new_folder)

        if not os.path.exists(dst_path):
            os.makedirs(dst_path)
        else:
            print_log("!Error copy_from_flash_drive - dir %s exists" % dst_path)
            sys.exit()

    else:
        dst_path = hard_drive

    for file_name in file_names:
        src_file_name = os.path.join(flash_path, file_name)
        dst_file_name = os.path.join(dst_path, file_name)

        check_not_exist(dst_file_name)
        check_not_exist(md5name(dst_file_name))

        utils.copyFile(src_file_name, dst_file_name)
        utils.copyFile(md5name(src_file_name), md5name(dst_file_name))

    return dst_path


def check_copied_from_flash(dst_folder, file_names):
    check_drive_dummys()

    buf = ""

    for file_name in file_names:
        file_name = os.path.join(dst_folder, file_name)

        hash_str = utils.calc_hash(file_name)
        ok = check_hash_str(hash_str, md5name(file_name))
        if ok:
            buf = file_name

    if buf:
        pyperclip.copy("veracrypt -t -k '' --protect-hidden=no --pim=1 " + buf + " /media/veracrypt63/")

def copy_to_flash_drive(flash_folder, file_names):
    check_drive_dummys()

    flash_folder = os.path.join(flash_drive, flash_folder)
    if not os.path.exists(flash_folder):
        os.makedirs(flash_folder)

    if g_home:
        src_path = get_last_folder(hard_drive)
        src_path = os.path.join(hard_drive, src_path)
    else:
        src_path = hard_drive
        
        
    #print_log(src_path)

    for file_name in file_names:

        src_file_name = os.path.join(src_path, file_name)

        calc_hash2file(src_file_name, md5name(src_file_name))

        dst_file_name = os.path.join(flash_folder, file_name)

        check_not_exist(dst_file_name)
        check_not_exist(md5name(dst_file_name))

        utils.copyFile(src_file_name, dst_file_name)
        utils.copyFile(md5name(src_file_name), md5name(dst_file_name))


def check_copied_to_flash(flash_folder, file_names):

    if not utils.query_yes_no('Eject flash and turn on again. Press \'y\' when ready'):
        print_log('!check interrupted')
    else:
        check_drive_dummys()

        flash_path = os.path.join(flash_drive, flash_folder)

        for file_name in file_names:
            file_path = os.path.join(flash_path, file_name)
            check_hash_str(utils.calc_hash(file_path), md5name(file_path))


def main_from_flash(file_names):

    global g_log

    if not utils.query_yes_no('Are you sure?'):
        return

    check_drive_dummys()

    #g_log = open(log_file_name, "w")

    move_delete_backups(file_names)

    flash_folder = get_flash_folder()
    dst_folder = copy_from_flash_drive(flash_folder, file_names)
    print_log('copied to ' + dst_folder)
    check_copied_from_flash(dst_folder, file_names)


def main_to_flash(file_names):

    global g_log

    if not utils.query_yes_no('Are you sure?'):
        return

    check_drive_dummys()

    #g_log = open(log_file_name, "w")

    flash_folder = get_new_folder(flash_drive, g_add_suffix)
    copy_to_flash_drive(flash_folder, file_names)
    print_log('copied to ' + flash_folder)
    check_copied_to_flash(flash_folder, file_names)
    

if __name__ == "__main__":
    assert False
