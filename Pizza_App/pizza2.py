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
from tkinter import messagebox
from tkinter import ttk
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
    ''''''
    for pizza_file_name in os.listdir(path):
        if pizza_file_name.lower().endswith(VALID_IMAGE_EXTENSIONS):
            pizza_name=os.path.splitext(pizza_file_name)[0]
            

    

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
    print("Add pizza button activated")

def del_pizza():
    print("Delete pizza button activated")

def quitApp(myApp):
    result=messagebox.askyesno("Quit?","Do you want to quit?")
    if result:
        myApp.destroy()
    else:
        messagebox.showinfo("Continue","You chose to not quit")

def configure_style():
    """
    Configure the visual style of the application, including button styles and themes.
    """
    pass

def create_frames(myApp):
    top_frame=tk.Frame(myApp,width=1200,height=50,bg='light gray')
    top_frame.grid(row=0,column=0,columnspan=2,sticky='nsew')
    top_frame.propagate(False)

    pizza_item_details_frame=tk.Frame(myApp,width=2000,height=300,bg='red')
    pizza_item_details_frame.grid(row=1,column=1,columnspan=2,sticky='nsew')
    pizza_item_details_frame.propagate(False)
    
    item_details_frame=tk.Frame(myApp,width=500,height=290,bg='black')
    item_details_frame.place(x=900,y=50)
    item_details_frame.propagate(False)

    order_details_frame=tk.Frame(myApp,width=2000,height=400,bg='green')
    order_details_frame.grid(row=2,column=0,columnspan=2,sticky='nsew')
    order_details_frame.propagate(False)

    return{
        "menu":top_frame,
        "pizza":pizza_item_details_frame,
        "details":item_details_frame,
        "cart":order_details_frame
    }

def create_buttons(frame, myApp, allPizzaDict, pizza_item_details_frame, item_details_frame, order_details_frame, pizza_cart, pizza_prices):
    ''' '''
    selected_pizza_name=tk.StringVar(value="")
    btn1=ttk.Button(frame,text="Show All Pizza")
    btn2=ttk.Button(frame,text="Clear All Pizza",state=tk.DISABLED)
    delete_button=ttk.Button(frame,text="Delete",state=tk.DISABLED)

    btn1.grid(row=0,column=0,padx=5,pady=5)
    btn2.grid(row=0,column=1,padx=5,pady=5)
    delete_button.grid(row=0,column=2,padx=5,pady=5)
    delete_button.config(command=lambda:del_pizza())

    btn1.config(command=lambda: pizza_images_as_buttons(btn1,btn2,allPizzaDict, pizza_item_details_frame, item_details_frame, order_details_frame, pizza_cart, pizza_prices))
    btn2.config(command=lambda:clear_all_frames(btn1, btn2,  pizza_item_details_frame, item_details_frame, order_details_frame,pizza_cart))

    add_pizza_btn=ttk.Button(frame,text="Add Pizza",command=lambda: add_pizza()).grid(row=0,column=3)
    quit_btn=ttk.Button(frame,text="Quit",command=lambda: quitApp(myApp)).grid(row=0,column=4)
    
def main():
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
    create_buttons(frames["menu"], myApp, allPizzaDict, frames["pizza"], frames["details"], frames["cart"], pizza_cart, pizza_prices)

    myApp.mainloop()

main()
