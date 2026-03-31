from array import *
from tkinter import *
from tkinter.font import Font
import tkinter.messagebox as messagebox
from datetime import datetime
from tkinter import Scrollbar

# called function for saving values
def save_values():
    values = [str(value) for value in array]

    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
    with open(filename, "w") as file:
        file.write("\n".join(values))

    messagebox.showinfo("Save Successful", "Input values have been saved.")


# called function to display array element by position
def display_by_position():
    try:
        position = int(display_position_entry.get())
        if 1 <= position <= len(array):
            value = array[position - 1]
            messagebox.showinfo("Array Element", f"The value at position {position} is: {value}")
        else:
            messagebox.showinfo("Position Error", "Invalid array position.")
    except ValueError:
        messagebox.showerror("Error", "Invalid Input Provided.")


# called function to replace array element with position
def replace_with_position():
    try:
        position = int(position_entry.get())
        if 1 <= position <= len(array):
            replacement = int(replace_entry.get())
            array[position - 1] = replacement
            list2.delete(0, END)
            for i, x in enumerate(array, start=1):
                list2.insert(END, f"{i}. {x}")
            messagebox.showinfo("Replacement Success", "Array element replaced successfully.")
        else:
            messagebox.showinfo("Replacement Failed", "Invalid array position.")
    except ValueError:
        messagebox.showerror("Error", "Invalid Input Provided.")

# called function to remove array element by position
def remove_by_position():
    try:
        position = int(remove_position_entry.get())
        if 1 <= position <= len(array):
            del array[position - 1]
            list2.delete(0, END)
            for i, x in enumerate(array, start=1):
                list2.insert(END, f"{i}. {x}")
            messagebox.showinfo("Removal Success", "Array element removed successfully.")
        else:
            messagebox.showinfo("Removal Failed", "Invalid array position.")
    except ValueError:
        messagebox.showerror("Error", "Invalid Input Provided.")


# called function for search value
def search_value():
    search_number = int(search_entry.get())
    if search_number in array:
        messagebox.showinfo("Search Result", "Value Present in the Array")
    else:
        messagebox.showinfo("Search Result", "Value is NOT Present in the Array")


# display array value
def display_value():
    list1.delete(0, END)  # Clear old numbers
    for i in range(len(array)):
        try:
            value = int(txt_box[i].get())
            array[i] = value
            print(f"value{value} save in {i}")
        except:
            messagebox.showerror("Error", "Invalid Input")
            return
    for i, x in enumerate(array, start=1):
        list1.insert(END, f"{i}. {x}")


# called function for insert value
def insert_value(n, data):
    list2.delete(0, END)
    array.insert(n - 1, data)
    for i, x in enumerate(array, start=1):
        list2.insert(END, f"{i}. {x}")


# called function for update value
def update_value(data1, data2):
    if data1 in array:
        list2.delete(0, END)
        n = array.index(data1)
        array[n] = data2
        for i, x in enumerate(array, start=1):
            list2.insert(END, f"{i}. {x}")
    else:
        messagebox.showinfo("Update Failed", "Number Doesn't Exist")



# called function for remove value
def remove_value(data):
    if data in array:
        list2.delete(0, END)
        array.remove(data)
        for i, x in enumerate(array, start=1):
            list2.insert(END, f"{i}. {x}")
    else:
        messagebox.showinfo("Remove Failed", "Number Doesn't Exist")

# create buttons for array display
def create_array(array_num):
    global i
    for i in range(array_num):
        index_label = Label(root, text=f"Cost-{i + 1}", font=("arial",9,"bold"), bg="white")
        index_label.place(x=5, y=115 + (i * 20))
        entry_box = Entry(root, bg="white")
        entry_box.place(x=80, y=115 + (i * 20))
        txt_box.append(entry_box)
        array.append(0)
        y = i

    # display button
    display_button = Button(root, text="Display", bd=0, padx=12, font=("arial",11,"bold"), bg="white", command=display_value)
    display_button.place(x=90, y=145 + (i * 20))

# Update an existing text box with the selected array value from list1
def on_list1_click(event):
    selected_index = list1.curselection()
    if selected_index:
        value = list1.get(selected_index)
        # Check if the selected item has the expected format
        parts = value.split('. ')
        if len(parts) == 2:
            # Extract the array value from the selected item
            array_value = parts[1]
            # Update the desired text box with the selected array value
            update_entry1.delete(0, END)  # Clear the current text in the text box
            update_entry1.insert(END, array_value)  # Set the selected array value in the text box
            remove_entry.delete(0, END)  # Clear the current text in the text box
            remove_entry.insert(END, array_value)  # Set the selected array value in the text box
        else:
            messagebox.showerror("Error", "Invalid selected item format.")

# Update an existing text box with the selected array value from list2
def on_list2_click(event):
    selected_index = list2.curselection()
    if selected_index:
        value = list2.get(selected_index)
        # Check if the selected item has the expected format
        parts = value.split('. ')
        if len(parts) == 2:
            # Extract the array value from the selected item
            array_value = parts[1]
            # Update the desired text box with the selected array value
            update_entry1.delete(0, END)  # Clear the current text in the text box
            update_entry1.insert(END, array_value)  # Set the selected array value in the text box
            remove_entry.delete(0, END)  # Clear the current text in the text box
            remove_entry.insert(END, array_value)  # Set the selected array value in the text box
        else:
            messagebox.showerror("Error", "Invalid selected item format.")



# main
root = Tk()
root.geometry("1350x750+8+1")
root.title("Daily Expenditure Tracker")
root.config(bg="#9fafca")



# list display
array_num_label = Label(root, relief="solid", text=" Cost Quantity:- ", font=("arial",15,"bold"), bg="white")
array_num_label.place(x=10, y=10)

array_num_entry = Entry(root, bg="#FFFFFF")
array_num_entry.place(x=15, y=45)

create_button = Button(root, text="ENTER", bd=0, padx=12, font=("arial",11,"bold"), bg="white",
                       command=lambda: create_array(int(array_num_entry.get())))
create_button.place(x=15, y=70)

# add
insert_label = Label(root, relief="solid", text=" Insertion Section:- ", font=("arial",15,"bold"), bg="white")
insert_label.place(x=570, y=15)
insert_label = Label(root, text="Enter Index No :", font=("arial",11,"bold"), bg="#9fafca")
insert_label.place(x=570, y=65)
insert_entry1 = Entry(root, bg="#FFFFFF")
insert_entry1.place(x=700, y=65)

insert_label = Label(root, text="Enter New Cost : ", font=("arial",11,"bold"), bg="#9fafca")
insert_label.place(x=570, y=95)
insert_entry2 = Entry(root, bg="#FFFFFF")
insert_entry2.place(x=700, y=95)


insert_button = Button(root, text="ADD", bd=0, padx=12, font=("arial",11,"bold"), bg="white",
                       command=lambda: insert_value(int(insert_entry1.get()), int(insert_entry2.get())))
insert_button.place(x=830, y=75)

# Update
update_label = Label(root, relief="solid", text=" Update Section:- ", font=("arial",15,"bold"), bg="white")
update_label.place(x=570, y=320)
update_label = Label(root, text="*Replace value using Value ", font=("arial",13,"bold"),fg="#00008B" ,bg="#9fafca")
update_label.place(x=565, y=360)
update_label = Label(root, text="Previous Value : ", font=("arial",11,"bold"), bg="#9fafca")
update_label.place(x=570, y=390)
update_entry1 = Entry(root, bg="#FFFFFF")
update_entry1.place(x=700, y=390)

update_label = Label(root, text="Desired Value : ", font=("arial",11,"bold"), bg="#9fafca")
update_label.place(x=570, y=415)

update_entry2 = Entry(root, bg="#FFFFFF")
update_entry2.place(x=700, y=415)

update_button = Button(root, text="UPDATE", bd=0, padx=12, font=("arial",11,"bold"), bg="white",
                       command=lambda: update_value(int(update_entry1.get()), int(update_entry2.get())))
update_button.place(x=830, y=400)

# delete
remove_label = Label(root, relief="solid", text=" Deletion Section:-", font=("arial",15,"bold"), bg="white")
remove_label.place(x=570, y=570)
remove_label = Label(root, text="Delete By Cost : ", font=("arial",11,"bold"), bg="#9fafca")
remove_label.place(x=570, y=615)
remove_entry = Entry(root, bg="#FFFFFF")
remove_entry.place(x=700, y=615)
remove_button = Button(root, text="DELETE", bd=0, padx=12, font=("arial",10,"bold"), bg="white",
                       command=lambda: remove_value(int(remove_entry.get())))
remove_button.place(x=830, y=615)


#search
search_label = Label(root, relief="solid", text=" Search Section:- ", font=("arial",15,"bold"), bg="white")
search_label.place(x=570, y=160)
search_label = Label(root, text="Search By Value : ", font=("arial", 11, "bold"), bg="#9fafca")
search_label.place(x=570, y=200)
search_entry = Entry(root, bg="#FFFFFF")
search_entry.place(x=700, y=200)
search_button = Button(root, text="SEARCH", bd=0, padx=12, font=("arial",10,"bold"), bg="white",
                       command=search_value)
search_button.place(x=830, y=200)

# save
save_button = Button(root, text=" SAVE ", bd=0, padx=30, bg="#FFFFFF", font=("arial", 12, "bold"), command=save_values)
save_button.place(x=1100, y=480)

# Replace with Position label and entry
position_label = Label(root, text="*Replace value using Index ", font=("arial",13,"bold"),fg="#00008B" ,bg="#9fafca")
position_label.place(x=565, y=445)
position_label = Label(root, text="Index No.:", font=("arial", 11, "bold"), bg="#9fafca")
position_label.place(x=570, y=475)
position_entry = Entry(root, bg="#FFFFFF")
position_entry.place(x=700, y=475)

# Replace with Value label and entry
replace_label = Label(root, text="Desired Value:", font=("arial", 11, "bold"), bg="#9fafca")
replace_label.place(x=570, y=500)
replace_entry = Entry(root, bg="#FFFFFF")
replace_entry.place(x=700, y=500)

# Replace button
replace_button = Button(root, text="REPLACE", bd=0, padx=12, font=("arial",11,"bold"), bg="white", command=replace_with_position)
replace_button.place(x=830, y=480)

# Remove by Position label and entry
remove_position_label = Label(root, text="Delete By Index:", font=("arial", 11, "bold"), bg="#9fafca")
remove_position_label.place(x=570, y=645)
remove_position_entry = Entry(root, bg="#FFFFFF")
remove_position_entry.place(x=700, y=645)

# Remove button
remove_button = Button(root, text="REMOVE", bd=0, padx=12, font=("arial",10,"bold"), bg="white", command=remove_by_position)
remove_button.place(x=830, y=645)

# Display by Position label and entry
display_position_label = Label(root, text="Search By Index:", font=("arial",11, "bold"), bg="#9fafca")
display_position_label.place(x=570, y=230)
display_position_entry = Entry(root, bg="#FFFFFF")
display_position_entry.place(x=700, y=230)

# Display button
display_button = Button(root, text="DISPLAY", bd=0, padx=12, font=("arial",10,"bold"), bg="white", command=display_by_position)
display_button.place(x=830, y=230)

# list1
frame1 = Frame(root)
frame1.place(x=240, y=60)
scrollbar1 = Scrollbar(frame1)
scrollbar1.pack(side=RIGHT, fill=Y)
list1 = Listbox(frame1, width=20, height=15, bd=0, bg="#FFFFFF", cursor="hand2", font=('Verdana', 16))
list1.configure(yscrollcommand=scrollbar1.set)
scrollbar1.configure(command=list1.yview)
list1.pack()

# list2
frame2 = Frame(root)
frame2.place(x=1000, y=60)
scrollbar2 = Scrollbar(frame2)
scrollbar2.pack(side=RIGHT, fill=Y)
list2 = Listbox(frame2, width=20, height=15, bd=0, bg="#FFFFFF", cursor="hand2", font=('Verdana', 16))
list2.configure(yscrollcommand=scrollbar2.set)
scrollbar2.configure(command=list2.yview)
list2.pack()

# list 1 & 2 display text
txt_box = []
array = array('i', [])

main_data_label = Label(root, relief="solid", text="| Primary Monitor |", font=("arial",16,"bold"), bg="white")
main_data_label.place(x=240, y=10)
update_data_label = Label(root, relief="solid", text="| Final Monitor |", font=("arial",16,"bold"), bg="white")
update_data_label.place(x=1000, y=10)

list1.bind("<<ListboxSelect>>", on_list1_click)
list2.bind("<<ListboxSelect>>", on_list2_click)  # Bind the click event to list2

root.mainloop()