#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import sys
import time
import operator

def main():
    T = int(sys.stdin.readline())

    for case in range(1,T+1):
        sys.stdout.write("Case #{}: {}\n".format(case, ans()))
        sys.stdin.readline()

def ans():
    line = sys.stdin.readline().rstrip()
    line += sys.stdin.readline().rstrip()
    line += sys.stdin.readline().rstrip()
    line += sys.stdin.readline().rstrip()

    if check(line, 'X'):
        return "X won"
    elif check(line, 'O'):
        return "O won"
    elif line.find('.') >= 0:
        return "Game has not completed"
    else:
        return "Draw"

def check(str, char):
    str = str.replace('T', char)
    l = list(str)
    for i in range(0,4):
        if l[4*i] == l[4*i+1] == l[4*i+2] == l[4*i+3] == char:
            return True
        if l[i] == l[i+4] == l[i+8] == l[i+12] == char:
            return True
    if l[0] == l[5] == l[10] == l[15] == char:
        return True
    if l[3] == l[6] == l[9] == l[12] == char:
        return True
    return False

if __name__ == '__main__':
    main()

