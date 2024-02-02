import hashlib
import os
import shutil
import sys
sys.path.insert(0, '/media/xxx63/r/python')
import utils

res_file_name = '_res.md5_'
res_file_name_short = '_res.md5_short'


def print_hash(res_arr, res_arr2, file_name):
    print(file_name)
    md5 = utils.calc_hash(file_name)
    
    s = md5 + "\t" + file_name
    res_arr.append(s)
    
    s2 = md5 + "\t" + os.path.basename(file_name)
    res_arr2.append(s2)


def print_hash_recursive(dir, files_set):
    res_arr = []
    res_arr2 = []
    for dirpath, dirnames, filenames in os.walk(dir):
        for f in filenames:
            if len(files_set) == 0 or f in files_set:
                print_hash(res_arr, res_arr2, os.path.join(dirpath, f))
    
    res_arr.sort()
    res_arr2.sort()

    with open (res_file_name, "w") as out:
        for s in res_arr:
            out.write(s + "\n")

    with open (res_file_name_short, "w") as out:
        for s in res_arr2:
            out.write(s + "\n")

def get_files(file_list):
    ret = []
    with open (file_list, "r") as f:
        for line in f:
            line = line.rstrip()
            jj = line.find('\t')
            if jj != -1:
                file_name = line[jj+1:]
                ret = ret + [os.path.basename(file_name)]
            
    return set(ret)

def process1_create_md5s():

    # filter for file names, if empty - then no filter
    file_list = ''
    #file_list = '/media/zzz/DISK_L/2compare_and_delete/123/0_res.md5_'
    
    files_set = set()
    if file_list:
        files_set = get_files(file_list)
    print(files_set)
    
    
    #dir = "/media/zzz/DISK_L/_main_data/video"
    #dir = "/media/zzz/DISK_E/_main_data/Photoes/__new_foto_Canon"
    dir = os.getcwd()
    
    print_hash_recursive(dir, files_set)


def get_first_word(line):
    words = line.split()
    if words:
        return words[0]
    else:
        return line

def get_last_word(line):
    words = line.split()
    if words:
        return words[-1]
    else:
        return line

def get_md5_set(file_name, allow_dupes = True):
    ret_lines = set()
    with open (file_name, "r") as f1:
        for line in f1.readlines():
            line2 = line.strip()
            line2 = get_first_word(line2) + "###" + os.path.split(get_last_word(line2))[-1]
            if not allow_dupes and line2 in ret_lines:
                print("!!!Duplicate in", file_name, line2)
                sys.exit()
            ret_lines.add(line2)
    return ret_lines

def process2_cmp_md5s(file_name1, file_name2):

    lines_set_1 = get_md5_set(file_name1)
    lines_set_2 = get_md5_set(file_name2)
    
    #print(lines_set_1)
    #print(lines_set_2)
    
    if lines_set_1 == lines_set_2:
        print("All OK, sets are equal, size is %d" % len(lines_set_2))
        return
    
    
    all_ok = True
    cnt = 0

    for line in lines_set_1:
        cnt += 1
        if not (line in lines_set_2):
            print("!!!Error " + line)
            all_ok = False

    if all_ok:
        print("All OK, compared %d" % cnt)
    

if __name__ == "__main__":
    
    file_name_1 = '/media/xxx/video.md5'
    file_name_2 = '/media/xxx/checksum.md5'
    
    #process1_create_md5s()
    process2_cmp_md5s(file_name_1, file_name_2)
