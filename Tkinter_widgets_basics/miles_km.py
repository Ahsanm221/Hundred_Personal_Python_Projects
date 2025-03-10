from tkinter import *


def miles_to_km():
    input_value = float(entry.get())
    miles_value = input_value * 1.6093
    km.config(text=str(miles_value))


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles = Label(text="Miles")
miles.grid(row=0, column=2)
is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=1, column=0)
km = Label(text="Km")
km.grid(row=1, column=2)

entry = Entry(width=7)
entry.insert(END, string="0")
entry.grid(row=0, column=1)

km = Label(text="0")
km.grid(row=1, column=1)

# calls action() when pressed
calculate = Button(text="Calculate", command=miles_to_km)
calculate.grid(row=2, column=1)

window.mainloop()
