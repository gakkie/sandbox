#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import sys
import time
import operator


class Solver:
    def solve(self):
        self.T = int(sys.stdin.readline())

        for case in range(1,self.T+1):
            sys.stdout.write("Case #{}: {}\n".format(case, self.ans()))
            sys.stdin.readline()

    def ans(self):
        self.line = sys.stdin.readline().rstrip()
        self.line += sys.stdin.readline().rstrip()
        self.line += sys.stdin.readline().rstrip()
        self.line += sys.stdin.readline().rstrip()

        if self.check(self.line, 'X'):
            return "X won"
        elif self.check(self.line, 'O'):
            return "O won"
        elif self.line.find('.') >= 0:
            return "Game has not completed"
        else:
            return "Draw"

    def check(self, str, char):
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
    sv = Solver()
    sv.solve()

