import sys


class NotStrError(Exception):
    def __init__(self, s):
        self.s = s
        # self.message = '{} is not a string'.format(str(s))
        self.message = '{} is not a string\n'.format(s)


def print_if_string(s):
    if isinstance(s, str):
        print(s)
    else:
        raise NotStrError(s)


# sys.stderr.write("Error")

try:
    # if_string('we')
    print_if_string(1)
except NotStrError as e:
    # print(e.message)
    sys.stderr.write(e.message)
finally:
    print('Done.')

