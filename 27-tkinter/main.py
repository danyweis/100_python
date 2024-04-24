from tkinter import *


def button_clicked():
    '''What happens after a click'''
    given_text = input.get()
    my_label.config(text=f"You wrote: {given_text}")


window = Tk()
window.title("My GUI")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a Label", font=("Courier", 24, "bold"))
my_label.grid(row=0, column=0)
# Button
my_button = Button(text="Click me", command=button_clicked)
my_button.grid(row=1, column=1)

new_button = Button(text="New Button")
new_button.grid(row=0, column=2)

# Entry
input = Entry(width=20)
input.grid(row=2, column=3)



window.mainloop()