# Array-Linked-List-Expenditure-Tracker

A basic desktop application built with Python and Tkinter to demonstrate array and linked list operations in different Python UI.


## Motivation

The goal of this project was to create a simple application to manage and manipulate arrays and linked list, showcasing various operations like insertion, deletion, search, and display through a graphical user interface (GUI).


## Project Purpose

This project was built as a basic academic project to practice data structure operations using a GUI based Python application.


## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [Screenshots](#screenshots)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- **Array Insertion**: Insert elements at a specified index.
- **Array Deletion**: Delete elements by value or index.
- **Array Search**: Search for a specific value or index in the array.
- **Array Update**: Update an element at a specific index.
- **Display Array**: View the contents of the array.
- **Simple GUI**: The user interface is built using Python's Tkinter library to provide a basic, interactive environment.


- **Node Insertion**: Insert nodes at the beginning, end, or any specified position in the linked list.
- **Node Deletion**: Delete nodes by position or by value.
- **Node Search**: Search for a node in the list by value or by position.
- **Linked List Display**: View the entire linked list through a GUI window.
- **Simple GUI**: The user interface is built using Python's Tkinter library to provide a basic, interactive environment.


  
## Technologies Used

- **Languages**:
  - Python
- **Libraries/Frameworks**:
  - **Tkinter**: Python's built-in GUI library for building the desktop application.
  - **Array module**: For handling array operations.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.x**: The project is built with Python. You can download it from [python.org](https://www.python.org/downloads/).
- Tkinter is usually included with Python installations.


## Installation & Setup

Follow these steps to get the project up and running on your local machine:
1.  **Clone the repository**:
    ```bash
    git clone https://github.com/aka-assB0T/array-linked-list-expenditure-tracker.git
    cd array-linked-list-expenditure-tracker
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment**:
    *   **On Windows**:
        ```bash
        .\venv\Scripts\activate
        ```
    *   **On macOS/Linux**:
        ```bash
        source venv/bin/activate
        ```

4.  **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Technologies Used

- **Languages**:
  - Python
- **Libraries/Frameworks**:
  - **Tkinter**: Python's built-in GUI library for building the desktop application.
  - **Pillow**: For any image processing or handling of the GUI assets (optional).

.

### Key Changes for Your Project:
1. **Linked List Operations**: Based on the operations in `linked.py`, I added relevant features for insertion, deletion, and search.
2. **GUI**: The Tkinter setup is reflected in the README for handling user input.
3. **No Database**: This version doesn't use a database like the previous complaint management system.

    

## Usage
To run the application, simply execute the `main.py` file:

```bash
python main.py
```

Upon launching:

The array management GUI window will open.
You will be presented with options to add, delete, search, and view elements in the array.
To add an element: Enter a value and specify the index where the element should be inserted.
To delete an element: Specify the element to delete by value or by index.
To search for an element: Enter the value or index to search for.
To update an element: Specify the index and the new value to replace the existing one.

Upon launching:

The linked list GUI window will open.
You will be presented with options to add, delete, search, and view nodes in the linked list.
To add a node: Enter a value and specify the position (beginning, end, or a particular position).
To delete a node: Specify the node to delete by position or by value.
To search for a node: Enter the node value or position.

## Project Structure

```
.
├── .gitignore                   # Specifies intentionally untracked files to ignore
├── README.md                    # This README file
├── array-old-backup.py          # First version of the array program
├── array-updated.py             # Final version of the array program
├── linked-list-incomplete.py    # Linked list version, incomplete for now
└── requirements.txt             # Lists Python dependencies
```


## Configuration
Array Operations: The array operations like insertion, deletion, search, and update are managed in the array_operations.py module.
UI Settings: Basic UI configurations such as window geometry, titles, and background colors are set within main.py.

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: git checkout -b feature/your-feature-name.
3. Implement your changes.
4. Commit your changes with a clear and descriptive message: git commit -m "feat: Add new feature X" or git commit -m "fix: Resolve bug Y".
5. Push your branch to your forked repository: git push origin feature/your-feature-name.
6. Open a Pull Request to the main branch of this repository.

Please ensure your code adheres to PEP 8 style guidelines.

## Screenshots

Run the program and see yourself.

## License

This project is licensed under the MIT License - see the [LICENSE](./assets/LICENSE) file for details.

## Acknowledgments
*   This project was developed as a university (North Western University, Khulna) lab project by [aka-assB0T](https://github.com/aka-assB0T).
.
