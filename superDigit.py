def superDigit(n, k):
    if n<10:
        return n
    n=str(n)
    sum1=0
    for i in n:
       sum1+= int(i)
    return superDigit(sum1*k,1)

