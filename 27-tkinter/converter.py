from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(pady=50, padx=50)

# Functions:


def convert():
    value = float(miles_input.get())
    value *= 1.609
    convert_value.config(text=f"{round(value, 2)}")


# Labels

miles = Label(text="Miles")
miles.grid(row=0, column=2)
miles.config(pady=5, padx=5)

km = Label(text="KM")
km.grid(row=1, column=2)
km.config(pady=5, padx=5)

convert_value = Label(text="0")
convert_value.grid(row=1, column=1)
convert_value.config(pady=5, padx=5)

is_equal = Label(text="is equal to")
is_equal.grid(row=1, column=0)
is_equal.config(pady=5, padx=5)

# Button

button = Button(text="Calculate", command=convert)
button.grid(row=2, column=1)
button.config(pady=5, padx=5)

# Entry

miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)
miles_input.focus()


window.mainloop()