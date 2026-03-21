



def recSum(n,ln):
    if(ln<=0):
        return 0
    return recSum(n,ln-1) + n[ln-1]

def sumArray(n):
    return recSum(n,len(n))


print(sumArray([1,2,3,4]))
   