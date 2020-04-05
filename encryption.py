import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    column=int(math.ceil(math.sqrt(len(s))))
    
    row=int(math.floor(math.sqrt(len(s))))
    if row*column<len(s):
        row=row+1
    k=[]
    loop=len(s)
    while loop>column:
        i=0
        column1=""
        while i<column:
            column1+=s[i]
            i+=1
        s=s[column:]
        k.append(column1)
        loop=len(s)
    k.append(s)
    yeni=[]
    z=""
    m=0
    while m<=row:
         z=""
         for i in range(0,len(k)):
             
             if k[i]!="":

                
                z+=k[i][0]
                k[i]=k[i][1:]
             else:
                 continue
             
                 

         yeni.append(z)
         m+=1
    result=""
    for i in yeni:
        result+=i
        result+=" "
    result=result[:-1]
    return result




        






if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
