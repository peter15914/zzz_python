import sys
from datetime import timedelta, date, datetime


def print_help():
    # scriptname = os.path.basename(sys.argv[0])
    print(
        'zzz script for generating list of dates for calendar.txt\n'
        # 'Usage: {name} <file path>\n'
        # .format(name = scriptname)
        )


def process():

    start_date = datetime.today()
    day_count = 49
    for single_date in (start_date + timedelta(n) for n in range(day_count)):
        print(";-------- " + single_date.strftime("%a - %Y-%m-%d, day %j").lower())


def main():
    process()


if __name__ == '__main__':
    main()
