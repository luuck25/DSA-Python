
def sum(input:list[int]):
   
    if len(input) == 0:
        return  0    

    first = input[0]

    return first + sum(input[1:])


print(sum([1,2,3,4,5]))


def fib(n):

    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fib(n-1) + fib(n-2)

def power(x,n):

    if x == 0:
        return 1
    
    return n * power(x-1,n)

print(power(4,2))

