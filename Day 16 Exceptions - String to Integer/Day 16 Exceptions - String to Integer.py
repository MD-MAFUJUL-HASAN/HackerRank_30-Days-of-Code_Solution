#!/bin/python3

import math
import os
import random
import re
import sys


S = input().strip()

try:
    print(int(S))
except ValueError:
    print("Bad String")
