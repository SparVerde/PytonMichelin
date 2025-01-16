# %%
div = 0
try:
    10/div
    print("The program should continue")
except:
    print("error occured")

# %%
"""
ZeroDivisionError
"""

# %%
div = 0
try:
    10/div
    print("The program should continue")
except ZeroDivisionError:
    print("ZeroDivisionError occured")

# %%
"""
ValueError
"""

# %%
div = '24j'
try:
   int(div)
   print("The program should continue")
except ZeroDivisionError:
    print("ZeroDivisionError occured")
except ValueError:
    print("ValueError occured")

# %%
"""
General exception
"""

# %%
div = '24j'
try:
   div+30
   print("The program should continue")
except ZeroDivisionError:
    print("ZeroDivisionError occured")
except:
    print("General occured")

# %%
"""
Finally
"""

# %%
div = 100
try:
   div+30
   print("The program should continue")
except ZeroDivisionError:
    print("ZeroDivisionError occured")
except:
    print("General occured")
finally:
    print('This line executed regardless of error occured')

# %%
"""
Error class are and there is inheritage
"""