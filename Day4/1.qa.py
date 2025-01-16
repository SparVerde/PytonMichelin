# %%
a_b_c = 10_000_000 #_ is a 1000 separator, but in name we can't have space
a_b_c

# %%
a,b,c=1000,2000,3000 #packing and unpacking
print(a, type(a))
d=10,2
print(d, type(d))

# %%
"""
Unpacking
"""

# %%
x,y = (10,2)
print('x=',x)
print('y=',y)

# %%
import math as matematics

# %%
matematics.pi

# %%
"""
do and catch not used in python, instead of catch to use for error? not try-catch but try -except
"""

# %%
"""
Set: for unique value
"""

# %%
a={1,2,3}
print(a, type(a))

# %%
"""
Dictionary
"""

# %%
a=dict(x=2)
a
print(a, type(a))

# %%
"""
Prefered way of dict definition; Dictionary is mutuble
"""

# %%
a={'x':2}

# %%
"""
Is value is empty
"""

# %%
x={}
if x:
    print('x is not empty')
else:
    print("x is empty")

# %%
x={'k'}
if x:
    print('x is not empty')
else:
    print("x is empty")

# %%
letters = ['l','a','k','a','j','a']
ch = 'a'
indexes = [i for i in range(len(letters)) if letters[i]== ch]
indexes