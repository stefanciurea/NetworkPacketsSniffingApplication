# Packages / Modules
from tkinter import *
from tkinter import messagebox
from scapy.all import *
from Capture import *
from os import path

# Main window (Tkinter's root)
root = Tk()
root.geometry("300x300")
root.resizable(False, False)
root.title('Sniffing tool')

# Input variables
time_input = StringVar()
input_path = StringVar()

# Make an object for Sniffing class
sniff_object = Capture()

# Make a frame
root_frame = Frame(root)
root_frame.pack()

# Time input
time_label = Label(root_frame, text="Sniffing time [seconds]:")
time_label.pack()
time_entry = Entry(root_frame, textvariable=time_input)
time_entry.pack(fill='x', expand=True)
time_entry.focus()

# Function used to display a massage after sniffing
def Show_Message_Sniffing():
    if(time_input.get().isdigit()):
        if Sniff(time_input.get()):
            messagebox.showinfo('Massage', 'Great sniffing! Your capture cointains ' + str(len(sniff_object.captures)) + ' elements.')
    else:
        messagebox.showinfo('Massage', 'The input is not a number.')

# Function used for sniffing
def Sniff(time):
    packages = sniff(timeout=int(time), prn=0, store=sniff_object)
    sniff_object.setter(packages)
    return True

# Function used to display a massage after pressing "Save as JSON" button
def Show_Massage_Save_as_JSON():
    if path.exists(input_path.get()):
        if(len(sniff_object.captures)>0):
            if sniff_object.Save_JSON_file():
                messagebox.showinfo('Massage', 'Saved!')
            else:
                messagebox.showinfo('Massage', 'Could not save! Check the path and try again.')
        else:
            messagebox.showinfo('Massage', 'You sniffed 0 elements. Try again!')
    else:
        messagebox.showinfo('Massage', 'The path does not exist!')

# Function used for "Show statistics" button (It calls a function that generates a graph)
def Show_Statistics():
    sniff_object.Statistics()

# "Sniff!" button
capture_button = Button(root_frame, text="Sniff!", command=Show_Message_Sniffing)
capture_button.pack(fill='x', expand=True, pady=10)

# Path input
path_label = Label(root_frame, text="Path:")
path_label.pack()
path_entry = Entry(root_frame, textvariable=input_path)
path_entry.pack(fill='x', expand=True)
path_entry.focus()

# "Save as JSON" button
json_button = Button(root_frame, text="Save as JSON", command=Show_Massage_Save_as_JSON)
json_button.pack(fill='x', expand=True, pady=10)

# "Show statistics" button
stats_button = Button(root_frame, text="Show statistics", command=Show_Statistics)
stats_button.pack(fill='x', expand=True, pady=10)

root.mainloop()