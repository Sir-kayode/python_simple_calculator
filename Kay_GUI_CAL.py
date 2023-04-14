#!/usr/bin/env python
# coding: utf-8

# In[1]:


#In this code, we create a GUI interface using Tkinter that allows the user to enter two numbers and an operator, and 
#then calculates the result when the user clicks the "Calculate" button. The result is then displayed in 
#a separate field on the GUI.


import tkinter as tk

#This imports the Tkinter module, which provides a toolkit for building GUIs in Python.

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title(" BAFO Simple Calculator GUI-Group2")

#This defines a class called Calculator that contains the logic for the calculator GUI. The __init__ method is 
#called when an instance of the class is created, and takes a master parameter that represents the parent widget 
#of the GUI. In this case, the master parameter is a Tk object representing the root window of the GUI. 
#The title method is called on the master object to set the title of the window to "Project-Simple Calculator in Python using GUI-Group2"

        # Create input fields for num1, num2, and operator
        self.num1_label = tk.Label(master, text="First number:")
        self.num1_label.grid(row=0, column=0, padx=5, pady=5)
        self.num1_entry = tk.Entry(master, width=20)
        self.num1_entry.grid(row=0, column=1, padx=5, pady=5)

        self.num2_label = tk.Label(master, text="Second number:")
        self.num2_label.grid(row=1, column=0, padx=5, pady=5)
        self.num2_entry = tk.Entry(master, width=20)
        self.num2_entry.grid(row=1, column=1, padx=5, pady=5)

        self.operator_label = tk.Label(master, text="Operator (+, -, *, /):")
        self.operator_label.grid(row=2, column=0, padx=5, pady=5)
        self.operator_entry = tk.Entry(master, width=20)
        self.operator_entry.grid(row=2, column=1, padx=5, pady=5)
#These lines of code create the input fields for the user to enter the first number, second number, and operator. tk.Label 
#objects are created to provide text labels for each input field, and tk.Entry objects are created to allow the user
#to enter the values. The grid method is called on each object to position it in the GUI grid.

        # Create button to perform calculation
        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=3, column=1, padx=5, pady=5)
#This creates a tk.Button object with the label "Calculate" and the self.calculate method as the command to be 
#executed when the button is clicked. The grid method is called to position the button in the GUI grid

        # Create output field for result
        self.result_label = tk.Label(master, text="Result:")
        self.result_label.grid(row=4, column=0, padx=5, pady=5)
        self.result_entry = tk.Entry(master, width=20)
        self.result_entry.grid(row=4, column=1, padx=5, pady=5)
#These lines of code create the output field for the result. Another tk.Label object is created to provide a 
#label for the field, and another tk.Entry object is created to display the result. The grid method is 
#called to position both objects in the GUI grid
        
    def calculate(kay):
        try:
            num1 = float(kay.num1_entry.get())
            num2 = float(kay.num2_entry.get())
            operator = kay.operator_entry.get()

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2
            else:
                raise ValueError("Invalid operator")

            kay.result_entry.delete(0, tk.END)
            kay.result_entry.insert(0, str(result))
        except ValueError as e:
            kay.result_entry.delete(0, tk.END)
            kay.result_entry.insert(0, str(e))

#This is the calculate method that is called when the user clicks the "Calculate" button. It gets the input values 
#for num1, num2, and operator from the input fields using the get method of the tk.Entry objects. It then performs 
#the calculation based on the value of the operator variable using a series of if/elif statements. If the operator 
#is not one of the four valid options, it sets result to an error message. The result is then displayed in the output 
#field using the delete and insert methods of the tk.Entry object.
#The try/except block is used to handle errors that may occur if the user enters invalid input. If the input cannot 
#be converted to a float using the float function, it sets the result to an error message.

root = tk.Tk()
app = Calculator(root)
root.mainloop()


# In[ ]:




