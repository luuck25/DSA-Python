

## Sum of N numbers

 # without recursion
def sumofN(n):
    sum =0
    for i in range(1,n+1):
        sum += i
    return sum

print(sumofN(5) )   

def sumofNrecursion(n):
    if n == 0 :return 0
    return n + sumofNrecursion(n-1)

print(sumofNrecursion(5))