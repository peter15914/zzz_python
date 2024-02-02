
import sys, os, time, difflib, argparse, shutil, filecmp
from datetime import datetime, timezone

def file_mtime(path):
    t = datetime.fromtimestamp(os.stat(path).st_mtime,
                               timezone.utc)
    return t.astimezone().isoformat()

def good_encoding(fromfile, tofile):

    ret = True

    try:
        with open(fromfile, encoding = 'utf-8') as ff:
            fromlines = ff.readlines()
        with open(tofile, encoding = 'utf-8') as tf:
            tolines = tf.readlines()
    except:
        ret = False

    return ret


def get_diff(fromfile, tofile):
    #print(fromfile)

    fromdate = file_mtime(fromfile)
    todate = file_mtime(tofile)
    try:
        with open(fromfile, encoding = 'utf-8') as ff:
            fromlines = ff.readlines()
        with open(tofile, encoding = 'utf-8') as tf:
            tolines = tf.readlines()
    except:
        print("!!!bad encoding " + fromfile)
        with open(fromfile, encoding = 'cp1251') as ff:
            fromlines = ff.readlines()
        with open(tofile, encoding = 'cp1251') as tf:
            tolines = tf.readlines()

    context_lines = 0

    diff = difflib.unified_diff(fromlines, tolines, fromfile, tofile, fromdate, todate, n=context_lines)

    ret = list(diff)

#    if len(ret) >= 2:
#        if ret[0][0:3] == "---" and ret[1][0:3] == "+++":
#            ret = ret[2:]

    return ret

"""
def test_01():

    fromfile = r"C:\zzz\wrk\19_osgnew\Viewer3D.qrc"
    tofile = r"C:\zzz\__tmp\wrk\19_osgnew\Viewer3D.qrc"

    diff = get_diff(fromfile, tofile)
    if (len(diff) > 0):
        sys.stdout.writelines(diff)
"""

def dir_to_dict(dirname):

    ret = {}
    for root, dirs, files in os.walk(dirname):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            rel_path = os.path.relpath(file_path, dirname)
            ret[rel_path] = file_path

    return ret

def main():

    proj_name = "21_faults"

    dirname_new = os.path.join(r"C:\zzz\wrk", proj_name)
    dirname_prev = os.path.join(r"C:\zzz\__tmp\_tmp_srcs_from_cosmopolis\012", proj_name)
    #dirname_new = r"C:\zzz\wrk\19_osgnew"
    #dirname_prev = r"C:\zzz\__tmp\_tmp_srcs_from_cosmopolis\007\19_osgnew"
    res_dir = os.path.join(r"C:\zzz\__tmp\wrk\035", proj_name)

    FullCopies = False
    #FullCopies = True

    unneeded_exts = {'.cfg', '.alut', '.user'}

    files1 = dir_to_dict(dirname_new)
    files2 = dir_to_dict(dirname_prev)

    for file_name in files1:

        res_filename = os.path.join(res_dir, file_name)

        ext = os.path.splitext(file_name)[1]
        if ext in unneeded_exts:
            continue

        if not files2.get(file_name):
            os.makedirs(os.path.dirname(res_filename), exist_ok = True)
            shutil.copyfile(files1[file_name], res_filename)
        elif (filecmp.cmp(files1[file_name], files2[file_name])):
            pass
        elif FullCopies:
            os.makedirs(os.path.dirname(res_filename), exist_ok = True)
            shutil.copyfile(files1[file_name], res_filename)
        else:
            if not good_encoding(files2[file_name], files1[file_name]):
                os.makedirs(os.path.dirname(res_filename), exist_ok = True)
                shutil.copyfile(files1[file_name], res_filename)
                continue

            diff = get_diff(files2[file_name], files1[file_name])
            if len(diff) == 0:
                continue

            os.makedirs(os.path.dirname(res_filename), exist_ok = True)

            diff_str = ''.join(diff)
            max_len = (int)(os.path.getsize(files1[file_name]) * 1.0)

            if len(diff_str) < max_len:
                with open(res_filename + ".diff", 'w', encoding="utf-8") as out:
                    out.write(diff_str)
            else:
                print("%d >= %d (%s)" % (len(diff_str), max_len, file_name))
                shutil.copyfile(files1[file_name], res_filename)


if __name__ == '__main__':
    main()
