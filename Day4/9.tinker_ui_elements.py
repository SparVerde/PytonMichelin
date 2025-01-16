import tkinter as tk

window = tk.Tk() #we create an object on class
print(window)

SCREEN_WIDTH=window.winfo_screenwidth()
SCREEN_HEIGHT=window.winfo_screenheight()

width=height=600
x=SCREEN_WIDTH//2-width//2
y=SCREEN_HEIGHT//2-height//2
window.geometry(f'{width}x{height}+{x}+{y}')

#to create elements
#layout:
#labels
label = tk.Label(window, text ='Two more days of fun') #ctrl + klick to visualize the class
label.pack()

label_2 = tk.Label(window, text ='what a great day')
label_2.pack()

#button
#button = tk.Button(window, text='push me')
#button.pack()
#command and count and counter example
counter = 0 # we should define a global variable for this
def count():
    global counter
    print('the button was pushed')
    counter +=1
    print(f'the button was pushed for {counter} times')
button = tk.Button(window,text='push me',command=count())  
button.pack()  

window.mainloop()