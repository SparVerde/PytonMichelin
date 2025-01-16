import tkinter as tk

window = tk.Tk() #we create an object on class
print(window)

SCREEN_WIDTH=window.winfo_screenwidth()
SCREEN_HEIGHT=window.winfo_screenheight()

width=height=600
x=SCREEN_WIDTH//2-width//2
y=SCREEN_HEIGHT//2-height//2
window.geometry(f'{width}x{height}+{x}+{y}')



window.mainloop()