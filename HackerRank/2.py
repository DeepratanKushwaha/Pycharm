import calendar
m, d, y = map(int,input().split())
print(calendar.day_name[calendar.weekday(y, m, d)])


exit()

import textwrap


def wrap(string, max_width):
    return textwrap.fill(string, max_width)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
