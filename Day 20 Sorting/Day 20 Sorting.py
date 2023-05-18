#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    num_swaps = 0
    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                tmp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = tmp
                num_swaps += 1

        if num_swaps == 0:
            break
    print('Array is sorted in {} swaps.'.format(num_swaps))
    print('First Element: {}'.format(a[0]))
    print('Last Element: {}'.format(a[-1]))