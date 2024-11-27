import tkinter as tk

def calculate():
    """
    Performs the calculation based on the selected operation and displays the result.
    """
    operation = operation_var.get()
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())

    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 == 0:
            result = "Error: Division by zero"
        else:
            result = num1 / num2

    result_label.config(text=f"Result: {result}")

def clear_fields():
    """
    Clears the input fields and the result label.
    """
    num1_entry.delete(0, tk.END)
    num2_entry.delete(0, tk.END)
    result_label.config(text="")

def validate_input(P):
    if str.isdigit(P) or P == "":
        return True
    else:
        return False

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Define the validation command globally
vcmd = window.register(validate_input)

# Create labels and entry fields
operation_label = tk.Label(window, text="Operation:")
operation_label.grid(row=0, column=0, sticky=tk.W)

operation_var = tk.StringVar(window)
operation_var.set("Add")
operation_dropdown = tk.OptionMenu(window, operation_var, "Add", "Subtract", "Multiply", "Divide")
operation_dropdown.grid(row=0, column=1)

num1_label = tk.Label(window, text="Number 1:")
num1_label.grid(row=1, column=0, sticky=tk.W)
num1_entry = tk.Entry(window, validate='key', validatecommand=(vcmd, '%P'))
num1_entry.grid(row=1, column=1)

num2_label = tk.Label(window, text="Number 2:")
num2_label.grid(row=2, column=0, sticky=tk.W)
num2_entry = tk.Entry(window, validate='key', validatecommand=(vcmd, '%P'))
num2_entry.grid(row=2, column=1)

# Create the calculate and clear buttons
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, sticky=tk.W)
clear_button = tk.Button(window, text="Clear", command=clear_fields)
clear_button.grid(row=3, column=1, sticky=tk.E)

# Create a label to display the result
result_label = tk.Label(window, text="")
result_label.grid(row=4, columnspan=2)

window.mainloop()
