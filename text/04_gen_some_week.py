import sys, os
from datetime import timedelta, date, datetime


def print_help():
    script_name = os.path.basename(sys.argv[0])
    print(
        'zzz script for generating week report file\n'
        'Usage: {name} <week number>\n'
        .format(name=script_name)
        )


def print_sep(title):
    print(';' + '-' * 91 + '\n' + ';---' + title + "\n")


def print_days(days, need_add):
    for day in days:
        print(day.strftime("%a //%Y-%m-%d, day %j").lower())
        if need_add:
            print('#<xx> day\n#<xx> activitywatch\n    desc\n    done')
        print('\n')


def process(week=1):

    days = []
    year = datetime.today().year

    cur_date = date(year, 1, 1) - timedelta(7)
    while cur_date <= date(year, 12, 31):
        cur_week = cur_date.isocalendar()[1]
        if cur_week == week:
            days.append(cur_date)
        cur_date += timedelta(1)

    print('')
    print_sep('reports')
    print_days(days, False)
    print_sep('plans')
    print_days(days, False)


def main():
    if sys.argv.__len__() != 2:
        print_help()
        sys.exit()

    process(int(sys.argv[1]))


if __name__ == '__main__':
    main()
