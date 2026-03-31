from array import *
from tkinter import *
from tkinter.font import Font
import tkinter.messagebox as messagebox


# display array value
def display_value():
    for i in range(len(array)):
        try:
            value = int(txt_box[i].get())
            array[i] = value
            print(f"value{value} save in {i}")
        except:
            messagebox.showerror("Error", "Invalid Input Provided.")
            return
    for x in array:
        list1.insert(END, x)


# called function for insert value
def insert_value(n, data):
    list2.delete(0, END)
    array.insert(n - 1, data)
    for x in array:
        list2.insert(END, x)


# called function for update value
def update_value(data1, data2):
    list2.delete(0, END)
    n = array.index(data1)
    array.remove(data1)
    array.insert(n, data2)

    for x in array:
        list2.insert(END, x)


# called function for remove value
def remove_value(data):
    list2.delete(0, END)
    array.remove(data)

    for x in array:
        list2.insert(END, x)


# create buttons for array display
def create_array(array_num):
    global i
    for i in range(array_num):
        index_label = Label(root, text=f"Cost-{i + 1}", font=("arial",11,"bold"), bg="white")
        index_label.place(x=5, y=115 + (i * 30))
        entry_box = Entry(root, bg="white")
        entry_box.place(x=80, y=115 + (i * 30))
        txt_box.append(entry_box)
        array.append(0)
        y = i

    # display button
    display_button = Button(root, text="Display", bd=0, padx=12, font=("arial",11,"bold"), bg="white", command=display_value)
    display_button.place(x=215, y=113 + (i * 30))


# main
root = Tk()
root.geometry("1200x500+70+100")
root.title("Daily Cost Tracker")
root.config(bg="#9a9db1")
font1 = Font(family="Corbel", size=15, weight="bold")
font2 = Font(family="Brush Script MT", size=12, weight="bold")

# list display


array_num_label = Label(root, text="Enter Number of Costs:", font=("arial",12,"bold"), bg="#9a9db1")
array_num_label.place(x=10, y=10)

array_num_entry = Entry(root, bg="#FFFFFF")
array_num_entry.place(x=15, y=45)

create_button = Button(root, text="ENTER", bd=0, padx=30, bg="#FFFFFF",
                       command=lambda: create_array(int(array_num_entry.get())))
create_button.place(x=15, y=70)

# add
insert_label = Label(root, text="Enter Position No :", font=("arial",12,"bold"), bg="#9a9db1")
insert_label.place(x=600, y=15)
insert_entry1 = Entry(root, bg="#FFFFFF")
insert_entry1.place(x=600, y=50)

insert_label = Label(root, text="Enter New Cost : ", font=("arial",12,"bold"), bg="#9a9db1")
insert_label.place(x=600, y=75)
insert_entry2 = Entry(root, bg="#FFFFFF")
insert_entry2.place(x=600, y=100)


insert_button = Button(root, text="   ADD   ", bd=0, padx=12, bg="#FFFFFF",
                       command=lambda: insert_value(int(insert_entry1.get()), int(insert_entry2.get())))
insert_button.place(x=600, y=125)

# Update
update_label = Label(root, text="Enter Cost Value : ", font=("arial",12,"bold"), bg="#9a9db1")
update_label.place(x=600, y=190)
update_entry1 = Entry(root, bg="#FFFFFF")
update_entry1.place(x=600, y=225)

update_label = Label(root, text="Enter Edited Value : ", font=("arial",12,"bold"), bg="#9a9db1")
update_label.place(x=600, y=248)

update_entry2 = Entry(root, bg="#FFFFFF")
update_entry2.place(x=600, y=272)

update_button = Button(root, text="  UPDATE  ", bd=0, bg="#FFFFFF",
                       command=lambda: update_value(int(update_entry1.get()), int(update_entry2.get())))
update_button.place(x=600, y=300)

# delete
remove_label = Label(root, text="Delete Cost : ", font=("arial",12,"bold"), bg="#9a9db1")
remove_label.place(x=600, y=350)
remove_entry = Entry(root, bg="#FFFFFF")
remove_entry.place(x=600, y=380)
remove_button = Button(root, text="REMOVE", bg="#FFFFFF", bd=0, padx=12,
                       command=lambda: remove_value(int(remove_entry.get())))
remove_button.place(x=600, y=405)

# list1
frame1 = Frame(root)
frame1.place(x=320, y=60)
list1 = Listbox(frame1, width=20, height=15, bd=0, bg="#FFFFFF", cursor="hand2", font=('Verdana', 16))
list1.pack()
# list2
frame2 = Frame(root)

frame2.place(x=900, y=60)
list2 = Listbox(frame2, width=20, height=15, bd=0, bg="#FFFFFF", cursor="hand2", font=('Verdana', 16))
list2.pack()

# list 1 & 2 display text
txt_box = []
array = array('i', [])

main_data_label = Label(root, relief="solid", text="| Added Cost List |", font=("arial",12,"bold"), bg="white")
main_data_label.place(x=320, y=8)
update_data_label = Label(root, relief="solid", text="| Updated Cost List |", font=("arial",12,"bold"), bg="white")
update_data_label.place(x=900, y=10)

root.mainloop()
