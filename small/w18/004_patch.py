
import sys, os, time, difflib, argparse, shutil, filecmp, subprocess
from datetime import datetime, timezone

def file_mtime(path):
    t = datetime.fromtimestamp(os.stat(path).st_mtime,
                               timezone.utc)
    return t.astimezone().isoformat()

def get_diff(fromfile, tofile):
#    print(fromfile)

    fromdate = file_mtime(fromfile)
    todate = file_mtime(tofile)
    try:
        with open(fromfile, encoding = 'utf-8') as ff:
            fromlines = ff.readlines()
        with open(tofile, encoding = 'utf-8') as tf:
            tolines = tf.readlines()
    except:
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

    dirname_diffs = r"/media/xxx63/_001/001/21_faults/"
    dirname_src = r"/media/xxx63/r/qt/21_faults_/"

    FullCopies = False

    files_diffs = dir_to_dict(dirname_diffs)
    files_src = dir_to_dict(dirname_src)

    for file_name_diff in files_diffs:

        ext = os.path.splitext(file_name_diff)[1]
        if ext != '.diff':
            continue
                    
        #print(file_name, os.path.splitext(file_name))

        file_name_src = os.path.splitext(file_name_diff)[0];

        full_filename_diff = os.path.join(dirname_diffs, file_name_diff)
        full_filename_src = os.path.join(dirname_src, file_name_src)

        #print(full_filename_diff, full_filename_src)
        subprocess.call(['patch', full_filename_src, full_filename_diff])


if __name__ == '__main__':
    main()
