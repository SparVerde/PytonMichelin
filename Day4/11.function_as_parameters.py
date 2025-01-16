def add(a,b):
    return a+b

def diff(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b

def do_operaytion(a,b,func):
    return func(a,b)

print(do_operaytion(30,50,add))
print(do_operaytion(30,399,diff))
print(do_operaytion(30,399,print))
print(add(20,10))