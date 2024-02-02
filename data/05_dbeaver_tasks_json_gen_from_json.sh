#!/usr/bin/env bash

#   depth
#python3 ./05_dbeaver_tasks_json_gen_from_json.py wrk/05_dbeaver_tasks_json_depth.txt wrk/well_172/curves_list_depth_172.json true >res

#   time
python3 ./05_dbeaver_tasks_json_gen_from_json.py wrk/05_dbeaver_tasks_json_time.txt wrk/well_172/curves_list_time_172.json false >res
