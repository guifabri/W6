import tkinter as tk
import csv
from tkinter import ttk

# Function to get inventory data from a CSV file
def get_inventory():
    inventory = []
    with open("inventory.csv", "r") as inventory_file:
        reader = csv.reader(inventory_file)
        for row in reader:
            inventory.append(row)
    return inventory

# Main function
def main():
    
    # Create the main window
    main_window = tk.Tk()
    main_window.configure(bg='lightblue')
    main_window.geometry("1300x620")
    custom_font = ("Times", 36)
    btn_font = ("Bauhaus 93", 24)

    # Create a label in the main window
    lbl_load_inventory = tk.Label(main_window, text="Welcome to Inventory Manager", font=custom_font, bg="sky blue")
    lbl_load_inventory.pack()

    # Create a Frame to contain the buttons
    button_frame = tk.Frame(main_window, bg='lightblue')
    button_frame.pack(pady=20)
    
    # Create a "Load Inventory" button
    btn_load_inventory = tk.Button(button_frame, text="Load Inventory", font=btn_font, background="Steel blue", fg="white")
    btn_load_inventory.pack(side="left", padx=10)
    
    # Create a container frame for the grid
    frame = ttk.Frame(main_window)
    frame.pack(fill='both', expand=True)
    
    # Create a canvas (declare it as a global variable)
    global canvas
    canvas = tk.Canvas(frame)
    canvas.pack(side='left', fill='both', expand=True)
    
    # Create a vertical scrollbar
    scrollbar_y = ttk.Scrollbar(frame, orient='vertical', command=canvas.yview)
    scrollbar_y.pack(side='right', fill='y')
    
    # Configure the canvas for vertical scrolling
    canvas.configure(yscrollcommand=scrollbar_y.set)
    
    # Create another frame inside the canvas to place the grid
    inner_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=inner_frame, anchor='nw')
    
    # Create a flag to check if the grid is already displayed
    grid_displayed = False
    
    def show_data_entry():
        nonlocal grid_displayed  # Use nonlocal to modify the flag variable
        main_window.title("Grid with Scrollbar")
        if not grid_displayed:
            # Create the grid using labels
            for i, row in enumerate(get_inventory()):
                for j, value in enumerate(row):
                    label = ttk.Label(inner_frame, text=value, width=20, relief='solid')
                    label.grid(row=i, column=j, padx=5, pady=5)
            grid_displayed = True  # Set the flag to True to indicate the grid is displayed
            # Update the scroll region to adapt to the size of the grid
            canvas.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))
    
    # Create a "Show Inventory" button
    btn_show_inventory = tk.Button(button_frame, text="Show Inventory", font=btn_font, background="Steel blue", fg="white")
    btn_show_inventory.config(command=show_data_entry)
    btn_show_inventory.pack(side="left", padx=10)

    main_window.mainloop()

# Check if this script is the main module
if __name__ == "__main__":
    main()