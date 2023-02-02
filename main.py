import tkinter

# Create window

window = tkinter.Tk()
window.title("Miles to kilometer Converter")
window.config(padx=20, pady=20)


########################################################################################################################
# Creating row 0 layout

# create miles entry

miles_entry = tkinter.Entry()
miles_entry.grid(row=0, column=1)

# create miles entry label

miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)

########################################################################################################################
# Creating row 1 layout

# Create "is equal to" label
is_equal_to_label = tkinter.Label(text="is equal to")
is_equal_to_label.grid(row=1, column=0)

# Create kilometers label
kilometer_label = tkinter.Label(text="0")
kilometer_label.grid(row=1, column=1)

# Create km label
km_label = tkinter.Label(text="Km")
km_label.grid(row=1, column=2)


########################################################################################################################
# Creating row 2 layout

# Create Calculate button


def calculate_click():
    miles = float(miles_entry.get())
    kilometers = miles * 1.609
    kilometer_label["text"] = f"{kilometers:.2f}"


calculate_button = tkinter.Button(text="Calculate", command=calculate_click)
calculate_button.grid(row=2, column=1)

window.mainloop()
