from tkinter import ttk
from tkinter import *


# FUNCTIONS
from functions import abstract


class Interface():



    def Create_widgets(self):

        # FIRST CREATED A LABEL FROM LABELFRAME FUNCTION ADD THE WINDOWS IN THIS CASE
        # USE self.root AND THE text(on lower)
        # BEFORE ADD GRID PROPERTIES 
        label =LabelFrame(self.root, text="Here go widgets")
        label.grid(row=0, column=0, columnspan=3)
        
        # LABELS
        Label(label, text="user: ").grid(row=1, column=0)
        Label(label, text="password: ").grid(row=2, column=0)

        # BUTTONS
        Button(label, text="click", command=abstract.greeting ).grid(row=3, column=0)
        Button(label, text="Sample" ).grid(row=3, column=1)
        


    def __init__(self,root):
        # GENERATE WINDOWS, AND INSTANCTIATE FROM MAIN CONDITIONAL
        self.root = root
        self.root.title('Generator to data')
        self.root.geometry("800x300")

        self.root.frame = Frame

        
        self.Create_widgets()
        self.root.mainloop()


if __name__ == "__main__":
    root = Tk()
    interface = Interface(root)


