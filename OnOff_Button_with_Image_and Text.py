#ON/OFF Button with Change Image and Text
from tkinter import *
root=Tk()
root.geometry('800x600')# set Diamension of window
root.title("ON/OFF Buttons")
root.iconbitmap("python_logo_icon.ico")# set icon of the Application 
global is_on# Create a global Variable name is_on
is_on =True# At initial Set variabel value to boolean True .

# Create a Label
my_label=Label(root,text="The Switch is ON",fg="green",font=("Helvetica",32))
my_label.pack(pady=20)

#Define our Switch function
def Switch():
    global is_on
    if is_on:
        on_button.config(image=off_image)
        my_label.config(text="The Switch is OFF",fg="gray")
        is_on=False
    else:
        on_button.config(image=on_image)
        my_label.config(text="The Switch is ON",fg="green")
        is_on=True

on_image =PhotoImage(file='OnLamp-icon.png')# set image for on
off_image =PhotoImage(file='OffLamp-icon.png')# set image for off
on_button=Button(root,image=on_image,borderwidth=0,width=500,height=130,command=Switch)
on_button.pack(pady=50)

root.mainloop()
