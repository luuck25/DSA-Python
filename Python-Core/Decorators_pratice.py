

"""
Docstring for Decorators_pratice
"""


# without arg
def greet_decorator(func):
    def wrapper():
        print("Hi, Welcome")
        func()
    return wrapper

@greet_decorator
def greet():
    print("How are you")


greet()  



#with args

def add_decorator(fun1):
    def wrapper(*args,**kargs):
        print("runnung add ")
        return fun1(*args,**kargs)
    return wrapper

@add_decorator
def add(a,b):
    return a+b


print(add(4,5))