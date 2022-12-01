#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    lists = sorted(dir(hidden_4))
    for i in range(len(lists)):
        if lists[i][0] != '_':
            print(f"{lists[i]}")
