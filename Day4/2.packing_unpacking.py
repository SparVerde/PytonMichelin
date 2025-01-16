# %%
"""
Change values via packing unpacking
"""

# %%
a=10
b=20
print('a=',a)
print('b=',b)
a,b=b,a
print('a=',a)
print('b=',b)

# %%
"""
#Too many value for packing: Number of values to unpacked must be equal to numbers and inverse
"""

# %%
a,b = 10,1,2

# %%
a,*b=1,2,3,4,5
print(b)

# %%
"""
Mark *:
"""

# %%
a,*b,c=1,2,3,4,5
print(c)

# %%
"""
"*" In use 
"""

# %%
def func_with_params(*parameters):
    print('parameters:', parameters, type(parameters))

func_with_params(2.3)

# %%
def func_with_params(first, second,*parameters):
    print('first parameters:', first, type(first))
    print('parameters:', parameters, type(parameters)) #if start with * parameters could be empty
    
func_with_params(2,3,4)

# %%
"""
** Matrk:
"""

# %%
def func_with_params(first, second,*args,**kargs): # ** dictionary
    print('first parameters:', first, type(first))
    print('args:', args, type(args))
    print('kargs:', kargs, type(kargs))
    print(kargs['dubai'])
    
func_with_params(2,3,4, generic='hello', dubai = 30)

# %%
def func_with_params(first, second,*a,**k): # ** dictionary, the order is count we canb't put first ** and then *
    print('first parameters:', first, type(first))
    print('args:', a, type(a))
    print('kargs:', k, type(k))
    print(k['dubai'])
    
func_with_params(2,3,4, generic='hello', dubai = 30)

# %%
def func_with_params(first, second,**k): # ** dictionary, the order is count we canb't put first ** and then *
    print('first parameters:', first, type(first))
    #print('args:', a, type(a))
    print('kargs:', k, type(k))
    print(k['dubai'])
    
func_with_params(2,3, generic='hello', dubai = 30)