#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    count=0
    for x in range(len(c)+1):
        if x+1<len(c)+1 or x+c[x+2]==0:
            x+=1
        count+1
        

        
    return count
a=[0, 0, 0, 0, 1, 0]
print(jumpingOnClouds(a))
