import tkinter as tk
from tkinter import simpledialog
from tkinter import scrolledtext

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get_values(self):
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return values

def show_popup_menu(event):
    popup_menu.post(event.x_root, event.y_root)

def create_new():
    # Ask for the number of digits to input
    digits = simpledialog.askinteger("Input Digits", "How many digits do you want to input?",
                                     parent=root, minvalue=1)
    if digits is not None:
        create_entry_boxes(digits)

def store_values():
    values = [entry.get() for entry in entry_boxes]
    for i, value in enumerate(values, start=1):
        linked_list.add_node(f"{i}. {value}")
    clear_entry_boxes()


def display_values():
    values = linked_list.get_values()
    display_text.delete(1.0, tk.END)
    for value in values:
        display_text.insert(tk.END, str(value) + "\n")
    display_text.insert(tk.END, f"\n----")
    display_text.insert(tk.END, f" Total : {len(values)} Nodes ")
    display_text.insert(tk.END, f"----\n")

def create_entry_boxes(num_boxes):
    global entry_boxes
    entry_boxes = []

    # Calculate the width and height of each entry box
    box_width = 10
    box_height = 20

    # Calculate the spacing between entry boxes
    spacing = 10

    # Calculate the starting position for the first entry box
    start_x = 20
    start_y = 20


    # Create the entry boxes
    for i in range(num_boxes):
        x = start_x + i * (box_height + spacing)
        y = start_y
        entry = tk.Entry(canvas, width=box_width)
        entry.place(x=x, y=y)
        entry_boxes.append(entry)

def clear_entry_boxes():
    for entry in entry_boxes:
        entry.delete(0, tk.END)

def search_value(value):
    current = linked_list.head
    while current:
        if current.data.split(". ")[1] == str(value):
            return "Yes"
        current = current.next
    return "No"



def search():
    # Ask for the value to search
    value = simpledialog.askstring("Search Value", "Enter a value to search:",
                                    parent=root)
    if value is not None:
        result = search_value(value)
        display_text.insert(tk.END, f"\nSearch Result: {result}")

def remove_value(value):
    previous = None
    current = linked_list.head

    while current:
        if current.data.split(". ")[1] == str(value):  # Compare extracted value
            if previous:
                previous.next = current.next
            else:
                linked_list.head = current.next
            return True
        previous = current
        current = current.next

    return False

def remove_by_position():
    # Ask for the position to remove
    position = simpledialog.askinteger("Remove Position", "Enter a position to remove:",
                                       parent=root)
    if position is not None:
        previous = None
        current = linked_list.head
        current_position = 1

        while current and current_position != position:
            previous = current
            current = current.next
            current_position += 1

        if current_position == position and current:
            if previous:
                previous.next = current.next
            else:
                linked_list.head = current.next
            display_text.insert(tk.END, f"\nRemoved position: {position}")
        else:
            display_text.insert(tk.END, f"\nInvalid position: {position}")


def remove():
    # Ask for the value to remove
    value = simpledialog.askstring("Remove Value", "Enter a value to remove:",
                                    parent=root)
    if value is not None:
        removed = remove_value(value)
        if removed:
            display_text.insert(tk.END, f"\nRemoved value: {value}")
        else:
            display_text.insert(tk.END, f"\nValue not found: {value}")



# Create the main window
root = tk.Tk()
root.geometry("1000x500+70+40")
root.title("Right-Click Example")

# Create a blank page
canvas = tk.Canvas(root, width=400, height=300, bg="lightblue")
canvas.pack(fill=tk.BOTH, expand=True)

# Create a popup menu
popup_menu = tk.Menu(root, tearoff=0)
popup_menu.add_command(label="New", command=create_new)

# Bind the popup menu to the canvas
canvas.bind("<Button-3>", show_popup_menu)

# Create a linked list instance
linked_list = LinkedList()

# Create buttons for saving and displaying values
save_button = tk.Button(root, text="Save Values", command=store_values)
save_button.pack(side=tk.LEFT, padx=10, pady=10)

display_button = tk.Button(root, text="Display Values", command=display_values)
display_button.pack(side=tk.LEFT, padx=10, pady=10)

# Create a display section
display_frame = tk.Frame(root, width=200, height=300, bg="lightgray")
display_frame.pack(side=tk.RIGHT, padx=10, pady=10)

display_label = tk.Label(display_frame, text="Display Section")
display_label.pack(pady=10)

# Create a scrolled text widget
display_text = scrolledtext.ScrolledText(display_frame, width=40, height=10)
display_text.pack(fill=tk.BOTH, expand=True)

# Create a scrollbar and associate it with the display_text widget
scrollbar = tk.Scrollbar(display_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
display_text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=display_text.yview)

search_button = tk.Button(root, text="Search", command=search)
search_button.pack(side=tk.LEFT, padx=10, pady=10)

remove_button = tk.Button(root, text="Remove", command=remove)
remove_button.pack(side=tk.LEFT, padx=10, pady=10)

# Create a button for removing by position
remove_by_position_button = tk.Button(root, text="Remove by Position", command=remove_by_position)
remove_by_position_button.pack(side=tk.LEFT, padx=10, pady=10)


# Start the tkinter event loop
root.mainloop()
