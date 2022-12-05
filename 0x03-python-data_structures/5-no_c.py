#!/usr/bin/python3
def no_c(my_string):
    new_string = ''
    if ("c" not in my_string) & ("C" not in my_string):
        return my_string
    for x in my_string:
        if (x != 'c') & (x != 'C'):
            new_string = new_string + x
    return (new_string)
