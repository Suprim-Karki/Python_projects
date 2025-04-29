'''
Starter template for programming coursework.

You must build your app by writing code for  the functions listed below.

Code for some of the functions has been provided.

The whole app is a composition of functions.

No GLOBAL variables and button functionality managed by use of lambda functions.

Student Name: ____________________

Student ID: ______________________

'''

import os
import csv
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk


def load_pizza_prices(csv_file):
    pizza_prices = {}
    try:
        with open(csv_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, price = row
                pizza_prices[name] = float(price)
    except Exception as e:
        print(f"Error reading pizza prices CSV: {e}")
    return pizza_prices

def save_images(path, image_dict):
    VALID_IMAGE_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')
    for filename in os.listdir(path):
        if filename.lower().endswith(VALID_IMAGE_EXTENSIONS):
            name = os.path.splitext(filename)[0]
            img = Image.open(os.path.join(path, filename))
            img = img.resize((80, 80))
            image_dict[name] = ImageTk.PhotoImage(img)
    

def pizza_images_as_buttons(btn1,btn2,images, pizza_item_details_frame, item_details_frame, order_details_frame, pizza_cart, pizza_prices):
    
    """
    Render dictionary images as buttons in the pizza_item_details_frame.
    Clicking a button loads the image and name into the item_details_frame.
    """
    pass


def load_image_in_frame(name, image, item_details_frame, order_details_frame, pizza_cart, pizza_prices):
    for widget in item_details_frame.winfo_children():
        widget.destroy()
    """
    Load the selected pizza image and details into the item_details_frame.
    Allow the user to specify the quantity and add the item to the cart.
    that will call add_to_cart function
    """
    pass
    #  "Add to Cart" button
    def add_to_cart():
        """
        Load the selected pizza image and details into the item_details_frame.
        Allow the user to specify the quantity and add the item to the cart.
        """

        # Clear the display frame
        for widget in item_details_frame.winfo_children():
            widget.destroy()

        # Update the cart frame
        update_order_details_frame(order_details_frame, pizza_cart)

    add_to_cart_button = ttk.Button(item_details_frame, text="Add to Cart", command=add_to_cart)
    add_to_cart_button.grid(row=7, column=1, columnspan=2, pady=10)

    cancel_button = ttk.Button(item_details_frame, text="Cancel", command=lambda: clear_frame(item_details_frame))
    cancel_button.grid(row=7, column=0,padx = 5, pady=5, sticky = "w")

def update_order_details_frame(order_details_frame, pizza_cart):
    for widget in order_details_frame.winfo_children():
        widget.destroy()

    cart_label = tk.Label(order_details_frame, text = "Your order details: ")
    cart_label.grid(row =0, column=0, columnspan=2, padx=10, pady =5)
    row = 1
    total_price = 0.0
    for name, details in pizza_cart.items():
        quantity = details["quantity"]
        price = details["price"]
        line_total = quantity * price
        total_price += line_total

        img_label = tk.Label(order_details_frame, image = details["image"], font=("Arial", 12))  # Placeholder for image
        img_label.grid(row=row, column=0, padx=0, pady=2, sticky="w")

        # Display the name
        name_label = tk.Label(order_details_frame, text=name, font=("Arial", 12))
        name_label.grid(row=row, column=0, padx=0, pady=2, sticky="w")

        # Display the quantity
        quantity_label = tk.Label(order_details_frame, text=f"Qty: {quantity}", font=("Arial", 12))
        quantity_label.grid(row=row, column=1, padx=2, pady=2, sticky="e")

        # Display the line total
        line_total_label = tk.Label(order_details_frame, text=f"Total: £{line_total:.2f}", font=("Arial", 12))
        line_total_label.grid(row=row, column=2, padx=2, pady=2, sticky="e")

        row += 1

    # Display the grand total
    grand_total_label = tk.Label(order_details_frame, text=f"Grand Total: £{total_price:.2f}", font=("Arial", 14, "bold"))
    grand_total_label.grid(row=row, column=0, columnspan=3, pady=10)

     # Add Cancel and Confirm buttons
    ttk.Button(order_details_frame, text="Cancel",style="big.TButton", width=12, command=lambda: clear_cart(order_details_frame, pizza_cart)).grid(row=row + 1, column=1, pady=10, sticky="e")
    ttk.Button(order_details_frame, text="Confirm",style="big.TButton", width=12, command=lambda: confirm_order(order_details_frame, pizza_cart)).grid(row=row + 1, column=2, pady=10, sticky="e")

def clear_all_frames(btn1, btn2,  pizza_item_details_frame, item_details_frame, order_details_frame,pizza_cart):
    """
    Clear all widgets from the specified frames and reset their backgrounds.
    """
    pass
    
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def clear_cart(order_details_frame, pizza_cart):
    """
    Clear the cart and update the order_details_frame with a message  "Your cart is empty"
    """
    pass

def confirm_order(order_details_frame, pizza_cart):
    """
    Clear the cart and update the order_details_frame with a message  "Order successfully placed!"
    """
    pass


def add_pizza():
    
    """
    Print message in console
    """
    pass

def del_pizza():
    """
    Print message in console
    """
    pass

def quitApp(myApp):
    """
    Prompt the user to confirm quitting the application.
    If confirmed, close the application.
    """
    pass

def configure_style():
    """
    Configure the visual style of the application, including button styles and themes.
    """
    pass

def create_frames(myApp):
    """
    Create and configure the main frames for the application UI.
    """
    pass


def create_buttons(frame, myApp, allPizzaDict, pizza_item_details_frame, item_details_frame, order_details_frame, pizza_cart, pizza_prices):
    """
    Create and configure buttons for the application UI.
    Assign commands to each button to handle user interactions.
    """
    pass

def main():
    """
    Main function to initialize the application, set up the UI, and start the main event loop.
    """
    myApp = tk.Tk()
    myApp.title("Online Pizza Store by Student-w123456")
    myApp.geometry("1200x1200")
    myApp.configure(background="red")

    configure_style()
    frames = create_frames(myApp)
   
    pathAllPizza = 'allPizza/'
    pizza_prices_csv = "pizza_prices.csv"

    allPizzaDict, pizza_cart, pizza_prices = {}, {}, load_pizza_prices(pizza_prices_csv)
    save_images(pathAllPizza, allPizzaDict)
    print(f"Number of pizza images: {len(allPizzaDict)}")

    # Create and configure buttons
    # create_buttons(frames["menu"], myApp, allPizzaDict, frames["pizza"], frames["details"], frames["cart"], pizza_cart, pizza_prices)

    myApp.mainloop()

main()
