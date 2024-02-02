import sys, os

def print_help():
    scriptname = os.path.basename(sys.argv[0])
    print(
        'Generate part of dbeaver''s tasks.json.\n'
        'Usage: {name} <template_file> <curves_list_file>\n'
        'Example:\n'
        '  {name} 03_dbeaver_tasks_json.txt 03_curves_list.txt \n'.format(name = scriptname))


def process_files_time(template_file, curves_list_file):

    template_lines = ""
    with open(template_file) as f:
        template_lines = f.read()

    # print(template_lines)

    jobs_count = 0

    with open(curves_list_file) as f:
        for curve_line in f.read().splitlines():
            # print(curve_line.split()[0], curve_line.split()[1])
            curve_id = curve_line.split()[0]
            curve_mnemo = curve_line.split()[1]
            pts_count = int(curve_line.split()[2])
            if (pts_count < 2):
                continue

            new_name = 'time_seconds_from_start_{0}_{1}'.format(curve_mnemo, curve_id)
            # print(new_name)

            new_str = template_lines.replace('time_seconds_from_start_ACTCOD_2', new_name)
            new_str = new_str.replace('from dado_tempo_perf where cvpe_cd_curva = 2)', 'from dado_tempo_perf where cvpe_cd_curva = {0})'.format(curve_id))

            print(new_str)
            jobs_count += 1

    for i in range(jobs_count):
        print('{"type": "streamTransferConsumer"},')


def process_files_depth(template_file, curves_list_file):

    template_lines = ""
    with open(template_file) as f:
        template_lines = f.read()

    # print(template_lines)

    jobs_count = 0

    with open(curves_list_file) as f:
        for curve_line in f.read().splitlines():
            # print(curve_line.split()[0], curve_line.split()[1])
            curve_id = curve_line.split()[0]
            curve_mnemo = curve_line.split()[1]

            new_name = 'depth_{0}_{1}'.format(curve_mnemo, curve_id)
            # print(new_name)

            new_str = template_lines.replace('depth_unique_table_name', new_name)
            new_str = new_str.replace('where cvpe_cd_curva=25500145160', 'where cvpe_cd_curva={0}'.format(curve_id))

            print(new_str)
            jobs_count += 1

    for i in range(jobs_count):
        print('{"type": "streamTransferConsumer"},')


def process_files(template_file, curves_list_file):
    if not os.path.exists(template_file):
        print("File %s doesn't exist" % template_file)
        sys.exit()

    if not os.path.exists(curves_list_file):
        print("File %s doesn't exist" % curves_list_file)
        sys.exit()

    # process_files_time(template_file, curves_list_file)
    process_files_depth(template_file, curves_list_file)


def main():
    if sys.argv.__len__() != 3:
        print_help()
        sys.exit()

    process_files(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()
