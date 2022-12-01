#!/usr/bin/python3
import hidden_4
i = 0
if __name__ == "__main__":
    lists = sorted(dir(hidden_4))
    while i < len(lists):
        if lists[i][0] != '_':
            print(lists[i])
        i += 1
