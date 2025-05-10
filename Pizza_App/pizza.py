'''
Starter template for programming coursework.

You must build your app by writing code for the functions listed baelow.

Code for some of the functions has been provided.

The whole app is a composition of functions.

No GLOBAL variables and button functionality managed by use of lambda functions.

Student Name: Suprim Karki

Student ID: w2158225"
'''

import os
import csv
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


# Loads pizza names and prices from a CSV file into a dictionary
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

# Loads and resizes images from a directory and stores them in a dictionary
def save_images(path, image_dict):
    VALID_IMAGE_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')
    for pizza_file_name in os.listdir(path):
        if pizza_file_name.lower().endswith(VALID_IMAGE_EXTENSIONS):
            pizza_name = os.path.splitext(pizza_file_name)[0]
            path_joined_image = Image.open(os.path.join(path, pizza_file_name))
            path_joined_image = path_joined_image.resize((80, 80))
            image_dict[pizza_name] = ImageTk.PhotoImage(path_joined_image)

# Displays pizza images as buttons that can be clicked to show details
def pizza_images_as_buttons(btn1, btn2, images, pizza_item_details_frame, item_details_frame, order_details_frame, pizza_cart, pizza_prices, selected_pizza_name, delete_button):
    clear_frame(pizza_item_details_frame)  
    # Set the background color of the frames to red
    pizza_item_details_frame.config(bg="red")
    item_details_frame.config(bg="black")
    order_details_frame.config(bg="green")
    row, column = 0, 0
    for pizza_name, pizza_image in images.items():
        frame = tk.Frame(pizza_item_details_frame)
        frame.grid(row=row, column=column, padx=5, pady=5)

        # Each button loads the selected pizza's details
        tk.Button(frame, image=pizza_image,
                  command=lambda pn=pizza_name, pi=pizza_image: load_image_in_frame(pn, pi, item_details_frame, order_details_frame, pizza_cart, pizza_prices, selected_pizza_name, delete_button)).pack()

        column += 1
        if column > 5:
            column = 0
            row += 1

    # Disable "Show" and enable "Clear" after loading images
    btn1.config(state=tk.DISABLED)
    btn2.config(state=tk.NORMAL)

# Loads a selected pizza's details and allows user to add to cart
def load_image_in_frame(name, image, item_details_frame, order_details_frame, pizza_cart, pizza_prices, selected_pizza_name, delete_button):
    for widget in item_details_frame.winfo_children():
        widget.destroy()
    selected_pizza_name.set(name)
    delete_button.config(state=tk.NORMAL)

    # Show pizza image, name, and price
    tk.Label(item_details_frame, image=image).grid(row=0, column=0, columnspan=2, pady=5)
    tk.Label(item_details_frame, text=name,font=("Arial", 12)).grid(row=1, column=0, columnspan=2)
    price = pizza_prices.get(name, 0.0)
    tk.Label(item_details_frame, text=f"Price: £{price:.2f}",font=("Arial", 12)).grid(row=2, column=0, columnspan=2)

    # Input box for quantity (default 1)
    tk.Label(item_details_frame, text="Quantity", font=("Arial", 12)).grid(row=3, column=0)
    pizza_quantity_variable = tk.Spinbox(item_details_frame, from_=1, to=1000, width=5, font=("Arial", 12))  # from_ and to define range
    pizza_quantity_variable.grid(row=3, column=1)

    # Inner function to add item to cart
    def add_to_cart():
        try:
            quantity = int(pizza_quantity_variable.get())
            if quantity<1 or quantity>1000:
                messagebox.showerror("Input Error", "The quantity should not be less than 1 and greater than 1000!")
            else:
                if name in pizza_cart:
                    pizza_cart[name]["quantity"] += quantity
                else:
                    pizza_cart[name] = {"quantity": quantity, "price": price, "image": image}
            # Clear the display frame
            for widget in item_details_frame.winfo_children():
                widget.destroy()
            #update the cart frame
            update_order_details_frame(order_details_frame, pizza_cart)
        except ValueError:
            messagebox.showerror("Input Error", "The quantity should be an integer!")
        
    add_to_cart_button = ttk.Button(item_details_frame, text="Add to Cart", command=add_to_cart)
    add_to_cart_button.grid(row=7, column=1, columnspan=2, pady=10)

    cancel_button = ttk.Button(item_details_frame, text="Cancel", command=lambda: clear_frame(item_details_frame))
    cancel_button.grid(row=7, column=0,padx = 5, pady=5, sticky = "w")

# Updates the cart frame to show current pizza selections and totals
def update_order_details_frame(order_details_frame, pizza_cart):
    for widget in order_details_frame.winfo_children():
        widget.destroy()

    cart_label = tk.Label(order_details_frame, text = "Your order details: ")
    cart_label.grid(row =0, column=0, columnspan=2, padx=10, pady =5)
    
    if not pizza_cart:  # Check if the cart is empty
        tk.Label(order_details_frame, text="Your cart is empty", font=("Arial", 12)).grid(row=1, column=0, columnspan=2)
        return  # Exit the function if the cart is empty

    row = 1
    total_price = 0.0
    for name, details in pizza_cart.items():
        quantity = details["quantity"]
        price = details["price"]
        line_total = quantity * price
        total_price += line_total

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

     # Add Cancel and Confirm buttons with updated Cancel command
    ttk.Button(order_details_frame, text="Cancel",style="big.TButton", width=12, command=lambda: cancel_order(order_details_frame, pizza_cart)).grid(row=row + 1, column=1, pady=10, sticky="e")
    ttk.Button(order_details_frame, text="Confirm",style="big.TButton", width=12, command=lambda: confirm_order(order_details_frame, pizza_cart)).grid(row=row + 1, column=2, pady=10, sticky="e")

# New function to clear cart and show "Your cart is empty" after Cancel
def cancel_order(order_details_frame, pizza_cart):
    clear_cart(order_details_frame, pizza_cart)
    tk.Label(order_details_frame, text="Your cart is empty", font=("Arial", 12)).grid(row=0, column=0)

# Clears all content in all relevant frames and resets state
def clear_all_frames(btn1, btn2, pizza_item_details_frame, item_details_frame, order_details_frame, pizza_cart, selected_pizza_name, delete_button):
    clear_frame(pizza_item_details_frame)
    clear_frame(item_details_frame)
    clear_cart(order_details_frame, pizza_cart)
    btn1.config(state=tk.NORMAL)
    btn2.config(state=tk.DISABLED)
    delete_button.config(state=tk.DISABLED)
    selected_pizza_name.set("")

     # Set the background color of the frames to red
    pizza_item_details_frame.config(bg="red")
    item_details_frame.config(bg="red")
    order_details_frame.config(bg="red")

# Clears all widgets from a given frame
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Clears the cart and resets the order details frame
def clear_cart(order_details_frame, pizza_cart):
    pizza_cart.clear()
    clear_frame(order_details_frame)
    # Removed "Your cart is empty" message here to prevent display on Clear All Pizzas

# Finalizes order and shows success message
def confirm_order(order_details_frame, pizza_cart):
    pizza_cart.clear()
    clear_frame(order_details_frame)
    messagebox.showinfo("Order confirmed","Order successfully placed!")
    tk.Label(order_details_frame, text="Your cart is empty",font=("Arial", 12)).grid(row=0, column=0)

# Shows the add pizza button is clicked on console 

def add_pizza():
    print("Add New button activated")
    
# Shows the delete pizza button is clicked on console
def del_pizza():
    print("Delete button activated")

# Quits the application after confirmation
def quitApp(myApp):
    reply=messagebox.askyesno("Quit?", "Do you want to quit?")
    if reply:
        myApp.quit()
    else:
        messagebox.showinfo("Continue","You chose not to quit.")

# Custom style for ttk buttons
def configure_style():
    style = ttk.Style()
    style.theme_use("clam")
    # Base style for all buttons
    style.configure("TButton",
                    font=("Arial", 10, "bold"),
                    foreground="dark blue",
                    background="#add8e6",
                    padding=8)
    style.map("TButton",
              background=[("pressed", "red"),   # red when pressed
                          ("active", "#87CEEB")],  # lighter blue when hovered
              foreground=[("disabled", "grey"),
                          ("active", "dark blue")])  # grey when disabled, dark blue when active

# Creates and returns all GUI frames used in the app
def create_frames(myApp):
    top_frame = tk.Frame(myApp, height=50, bg="light grey")
    top_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
    top_frame.grid_propagate(False)

    pizza_item_details_frame = tk.Frame(myApp, bg="red", width=600, height=300)
    pizza_item_details_frame.config(width=2000, height=300)
    pizza_item_details_frame.grid(row=1, column=0, sticky="nsew")
    pizza_item_details_frame.grid_propagate(False)

    item_details_frame = tk.Frame(myApp, bg="black", width=400, height=300)
    item_details_frame.place(x=900, y=50)
    item_details_frame.config(width=500, height=290)
    item_details_frame.grid_propagate(False)

    order_details_frame = tk.Frame(myApp, bg="green", height=400)
    order_details_frame.grid(row=2, column=0, columnspan=2, sticky="nsew")
    order_details_frame.grid_propagate(False)

    return {
        "menu": top_frame,
        "pizza": pizza_item_details_frame,
        "details": item_details_frame,
        "cart": order_details_frame
    }

# Adds all buttons to the top menu frame
def create_buttons(frame, myApp, allPizzaDict, pizza_item_details_frame, item_details_frame, order_details_frame, pizza_cart, pizza_prices):
    selected_pizza_name = tk.StringVar(value="")
    btn1 = ttk.Button(frame, text="Show All Pizzas")
    btn2 = ttk.Button(frame, text="Clear All Pizzas", state=tk.DISABLED)
    delete_button = ttk.Button(frame, text="Delete", state=tk.DISABLED)

    btn1.config(command=lambda:
                pizza_images_as_buttons(btn1, btn2, allPizzaDict, pizza_item_details_frame,item_details_frame, order_details_frame, pizza_cart,pizza_prices, selected_pizza_name, delete_button))

    btn2.config(command=lambda: clear_all_frames(btn1, btn2, pizza_item_details_frame, item_details_frame,order_details_frame, pizza_cart, selected_pizza_name, delete_button))

    delete_button.config(command=lambda:del_pizza())

    btn1.grid(row=0, column=0, padx=5, pady=5)
    btn2.grid(row=0, column=1, padx=5, pady=5)
    delete_button.grid(row=0, column=2, padx=5, pady=5)

    ttk.Button(frame, text="Add New",command=lambda:add_pizza()).grid(row=0,column=3,padx=5,pady=5)

    ttk.Button(frame, text="Quit", command=lambda: quitApp(myApp)).grid(row=0, column=4, padx=5, pady=5)

# Main entry point for the app
def main():
    myApp = tk.Tk()
    myApp.title("Online Pizza Store by Student-w2158225")
    myApp.geometry("1200x800")
    configure_style()
    frames = create_frames(myApp)

    pathAllPizza = 'allPizza/'
    pizza_prices_csv = "pizza_prices.csv"

    allPizzaDict, pizza_cart, pizza_prices = {}, {}, load_pizza_prices(pizza_prices_csv)
    save_images(pathAllPizza, allPizzaDict) 
    print(f"Number of pizza images: {len(allPizzaDict)}")

     # Creating and configuring buttons

    create_buttons(frames["menu"], myApp, allPizzaDict, frames["pizza"], frames["details"], frames["cart"],pizza_cart, pizza_prices)

    myApp.mainloop()

main()
