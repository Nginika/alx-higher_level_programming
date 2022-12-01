#!/usr/bin/python3
import sys
if __name__ == "__main__":
    largs = sys.argv
    arg_count = len(largs)
    sum = 0
    for i in range(1, arg_count):
        sum = sum + int(largs[i])
    print(f'{sum:d}')
