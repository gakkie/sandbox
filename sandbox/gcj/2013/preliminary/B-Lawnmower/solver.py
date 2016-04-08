#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import sys
import time
import operator

class Solver:
    def solve(self):
        self.T = int(sys.stdin.readline())

        for case in range(1,self.T+1):
            n = sys.stdin.readline().rstrip().split(' ')
            sys.stdout.write("Case #{}: {}\n".format(case, self.__ans(int(n[0]), int(n[1]))))

    def __ans(self, a, b):
        board = []
        for i in range(1, a+1):
            board.append(sys.stdin.readline().rstrip().split(' '))
        print(board)

        return b


if __name__ == '__main__':
    s = Solver()
    s.solve()


