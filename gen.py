import sys

from aggregate.line import aggregate

if __name__ == '__main__':
    args = sys.argv
    if 1 < len(args): aggregate(args[1])
