import sys, os, json
from pathlib import Path

def print_help():
    scriptname = os.path.basename(sys.argv[0])
    print(
        'Generate last files from files with curve data.\n'
        'Usage: {name} <source directory with curve data> <dest directory for las files> <las_header_file> <curves_list_file>\n'
        'Example:\n'
        '  {name} ./wrk ./tmp_res_las las_header.txt curves_list.json\n'.format(name = scriptname))


def create_las_file(src_file_name, dest_file_name, file_name_base, las_header_file, curves_dict):

    las_header = ""
    with open(las_header_file) as f:
        las_header = f.read()

    gis_data = ""
    with open(src_file_name) as f:
        gis_data = f.read()

    curve_id = int(file_name_base.split('_')[-4])
    # print(curve_id)

    json_rec = curves_dict[curve_id]

    curve_mnemo = json_rec["mnemonico_contratada"].strip()
    null_value = json_rec["valor_nulo"]
    well_id = json_rec["codigo_poco"]
    well_name = json_rec["well_name"]

    gis_data = gis_data.replace('"diff_sec" "value_"\n', "")
    gis_data = gis_data.replace('"depth" "value"\n', "")
    las_header = las_header.replace('<null_value>', str(null_value))
    las_header = las_header.replace('<well_name>', well_name)
    las_header = las_header.replace('<well_id>', str(well_id))
    las_header = las_header.replace('<curve_mnemo>', 'd_' + curve_mnemo)

    f_res = open(dest_file_name, 'w')

    f_res.write(las_header)
    f_res.write(gis_data)

    f_res.close()


def process_files(src_dir, dest_las_dir, las_header_file, curves_list_file_json):
    if not os.path.exists(src_dir):
        print("Directory %s doesn't exist" % src_dir)
        sys.exit()

    if not os.path.exists(dest_las_dir):
        print("Directory %s doesn't exist" % dest_las_dir)
        sys.exit()

    if not os.path.exists(las_header_file):
        print("File %s doesn't exist" % las_header_file)
        sys.exit()

    if not os.path.exists(curves_list_file_json):
        print("File %s doesn't exist" % curves_list_file_json)
        sys.exit()

    curves_dict = {}

    with open(curves_list_file_json) as f:

        json_data = json.load(f)
        
        for json_rec in json_data:
            curve_id = json_rec["codigo_curva"]

            curves_dict[curve_id] = json_rec

    # print(curves_dict)

    for root, dirs, files in os.walk(src_dir):
        for file_name in files:
            if not file_name.endswith(".csv"):
                continue

            file_name_base = Path(Path(file_name).stem).stem
            # print(file_name_base)
            create_las_file(os.path.join(root, file_name), os.path.join(dest_las_dir, file_name_base + ".las"), file_name_base, las_header_file, curves_dict)


def main():
    if sys.argv.__len__() != 5:
        print_help()
        sys.exit()

    process_files(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])


if __name__ == '__main__':
    main()
