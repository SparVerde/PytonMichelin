import tkinter as tk
from tkinter import messagebox
import time
import random

#Constant convention:  CAPITAL LETTER
I_AM_NOT_HUNGRY='I am not hungry'
I_AM_HUNGRY='I am hungry'
I_AM_HAPPY='I am happy'

DONT_FEED_ME ="Don't feed me"
FEED_ME ="Feed me"

WINDOW_SIZE = 500

main_window = tk.Tk() #we create an object on class
status_label = tk.Label(main_window, text=I_AM_NOT_HUNGRY)
status_label.pack()
#status_label.grid(row=0,column=1) #we can use grid but everywhere we should use grid

#feed_button = tk.Button(main_window, text=DONT_FEED_ME)
#feed_button.pack()

new_frame=tk.Frame(main_window)
new_frame.pack()

is_hungry = False
is_game_running =True

def give_food():
    global is_game_running
    if not is_game_running:
        return
    
    print("give food was called")
    #time.sleep(5)
    #We read only global variant
    if is_hungry:
        print('You win')
        stop_time = time.time()
        delta = stop_time-start_time
        messagebox.showinfo(title='Congrats!',message=f'You win in {delta} seconds!')
        status_label.config(text = I_AM_HAPPY)
        feed_button.config(text=DONT_FEED_ME)
    else:
        print('You lose')
        messagebox.showerror(title='!Uuuu!', message='You lost my friend!')



def show_i_am_hungry():
    global is_hungry

    print("Tamagochi is hungry")
    status_label.config(text=I_AM_HUNGRY)
    feed_button.config(text=FEED_ME)
    is_hungry = True


#here we can put as grid after taking new_frame
feed_button = tk.Button(new_frame, text=DONT_FEED_ME, command=give_food)
feed_button.grid()
#give_food()



main_window.geometry(f'{WINDOW_SIZE}x{WINDOW_SIZE}')

status_label.after(3000, show_i_am_hungry)
start_time = time.time()

main_window.mainloop()