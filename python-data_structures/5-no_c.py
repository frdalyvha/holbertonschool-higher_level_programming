#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            result += ch
    return result
