import sys, os, json

def print_help():
    scriptname = os.path.basename(sys.argv[0])
    print(
        'Generate part of dbeaver''s tasks.json.\n'
        'Usage: {name} <template_file> <curves_list_json_file> <is_depth flag>\n'
        'Example:\n'
        '  {name} 05_dbeaver_tasks_json.txt 05_curves_list.json true\n'.format(name = scriptname))

def process_files_ex(template_file, curves_list_file_json, is_depth):

    template_lines = ""
    with open(template_file) as f:
        template_lines = f.read()

    # print(template_lines)

    jobs_count = 0

    with open(curves_list_file_json) as f:

        json_data = json.load(f)

        for json_rec in json_data:
            # print(json_rec["codigo_curva"])

            curve_id = json_rec["codigo_curva"]
            curve_mnemo = json_rec["mnemonico_contratada"].strip()
            well_id = json_rec["codigo_poco"]

            if is_depth:
                new_name = 'depth_{0}_{1}'.format(curve_mnemo, curve_id)
                # print(new_name)

                new_str = template_lines.replace('depth_unique_table_name', new_name)
                new_str = new_str.replace('where cvpe_cd_curva=25500145160', 'where cvpe_cd_curva={0}'.format(curve_id))
                new_str = new_str.replace('and poco_cd_poco=48259)', 'and poco_cd_poco={0})'.format(well_id))
                

                print(new_str)
            else:
                # time cures
                new_name = 'time_seconds_from_start_{0}_{1}'.format(curve_mnemo, curve_id)
                # print(new_name)

                new_str = template_lines.replace('time_seconds_from_start_ACTCOD_2', new_name)
                new_str = new_str.replace('from dado_tempo_perf where cvpe_cd_curva = 2)', 'from dado_tempo_perf where cvpe_cd_curva = {0})'.format(curve_id))

                print(new_str)

                
            jobs_count += 1

    for i in range(jobs_count):
        print('{"type": "streamTransferConsumer"},')


def process_files(template_file, curves_list_file, is_depth):
    if not os.path.exists(template_file):
        print("File %s doesn't exist" % template_file)
        sys.exit()

    if not os.path.exists(curves_list_file):
        print("File %s doesn't exist" % curves_list_file)
        sys.exit()

    process_files_ex(template_file, curves_list_file, is_depth)


def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    # else:
    #     raise argparse.ArgumentTypeError('Boolean value expected.')

    return False
    
def main():
    if sys.argv.__len__() != 4:
        print_help()
        sys.exit()

    process_files(sys.argv[1], sys.argv[2], str2bool(sys.argv[3]))

if __name__ == '__main__':
    main()
