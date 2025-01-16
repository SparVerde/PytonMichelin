#global variable, but inside function there is local variable
variable = 10 #global variable

def func():
    #local variable
    global variable #we should add global variable
    print(variable)
    variable+=1

func()
print(variable)



