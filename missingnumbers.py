import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.




def missingNumbers(arr,brr):
    listt=[]
    for a in brr:
        if a in arr:
            arr.remove(a)
        else:
            listt.append(a)
    for c in listt:
        sayi=listt.count(c)
        while sayi>1:
            listt.remove(c)
            sayi=listt.count(c)
    def quicksort(l):
        if l==[]:
            return l
        else:
            pivot=l[0]
            ls=[x for x in l[1:] if x<pivot]
            lg=[x for x in l[1:] if x>=pivot]
        return quicksort(ls)+[pivot]+quicksort(lg)
    listt=quicksort(listt)

    return listt
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    m = int(raw_input())

    brr = map(int, raw_input().rstrip().split())

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
