'''
Starter template for programming coursework.

You must build your app by writing code for the functions listed baelow.

Code for some of the functions has been provided.

The whole app is a composition of functions.

No GLOBAL variables and button functionality managed by use of lambda functions.

Student Name: ____________________

Student ID: ______________________

'''

import os
import csv
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

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
    for pizza_file_name in os.listdir(path):
        if pizza_file_name.lower().endswith(VALID_IMAGE_EXTENSIONS):
            pizza_name = os.path.splitext(pizza_file_name)[0]
            path_joined_image = Image.open(os.path.join(path, pizza_file_name))
            path_joined_image = path_joined_image.resize((80, 80))
            image_dict[pizza_name] = ImageTk.PhotoImage(path_joined_image)


def pizza_images_as_buttons(btn1, btn2, images, pizza_item_details_frame, item_details_frame, order_details_frame, pizza_cart, pizza_prices, selected_pizza_name, delete_button):
    clear_frame(pizza_item_details_frame)
    row, col = 0, 0
    for name, img in images.items():
        frame = tk.Frame(pizza_item_details_frame)
        frame.grid(row=row, column=col, padx=5, pady=5)

        tk.Button(frame, image=img,
                  command=lambda n=name, i=img: load_image_in_frame(n, i, item_details_frame, order_details_frame, pizza_cart, pizza_prices, selected_pizza_name, delete_button)).pack()

        col += 1
        if col > 5:
            col = 0
            row += 1

    if btn1 and btn2:
        btn1.config(state=tk.DISABLED)
        btn2.config(state=tk.NORMAL)

def load_image_in_frame(name, image, item_details_frame, order_details_frame, pizza_cart, pizza_prices, selected_pizza_name, delete_button):
    selected_pizza_name.set(name)
    if delete_button:
        delete_button.config(state=tk.NORMAL)

    clear_frame(item_details_frame)

    tk.Label(item_details_frame, image=image).grid(row=0, column=0, columnspan=2, pady=5)
    tk.Label(item_details_frame, text=name).grid(row=1, column=0, columnspan=2)
    price = pizza_prices.get(name, 0.0)
    tk.Label(item_details_frame, text=f"Price: £{price:.2f}").grid(row=2, column=0, columnspan=2)

    tk.Label(item_details_frame, text="Quantity").grid(row=3, column=0)
    qty_var = tk.StringVar(value="1")
    qty_menu = ttk.Combobox(item_details_frame, textvariable=qty_var, values=[str(i) for i in range(1, 6)], width=5)
    qty_menu.grid(row=3, column=1)

    def add_to_cart():
        qty = int(qty_var.get())
        if name in pizza_cart:
            pizza_cart[name]["quantity"] += qty
        else:
            pizza_cart[name] = {"quantity": qty, "price": price, "image": image}
        update_order_details_frame(order_details_frame, pizza_cart)
        clear_frame(item_details_frame)

    ttk.Button(item_details_frame, text="Cancel", command=lambda: clear_frame(item_details_frame)).grid(row=4, column=0, pady=5)
    ttk.Button(item_details_frame, text="Add to Cart", command=add_to_cart).grid(row=4, column=1, pady=5)

def update_order_details_frame(order_details_frame, pizza_cart):
    clear_frame(order_details_frame)
    tk.Label(order_details_frame, text="Your order details: ").grid(row=0, column=0, columnspan=3, padx=10, pady=5)
    row = 1
    total_price = 0.0
    for name, details in pizza_cart.items():
        quantity = details["quantity"]
        price = details["price"]
        line_total = quantity * price
        total_price += line_total

        tk.Label(order_details_frame, text=name).grid(row=row, column=0, sticky="w")
        tk.Label(order_details_frame, text=f"Qty: {quantity}").grid(row=row, column=1, sticky="e")
        tk.Label(order_details_frame, text=f"Total: £{line_total:.2f}").grid(row=row, column=2, sticky="e")
        row += 1

    tk.Label(order_details_frame, text=f"Grand Total: £{total_price:.2f}", font=("Arial", 14, "bold")).grid(row=row, column=0, columnspan=3, pady=10)
    ttk.Button(order_details_frame, text="Cancel", width=12, command=lambda: clear_cart(order_details_frame, pizza_cart)).grid(row=row + 1, column=1, pady=10, sticky="e")
    ttk.Button(order_details_frame, text="Confirm", width=12, command=lambda: confirm_order(order_details_frame, pizza_cart)).grid(row=row + 1, column=2, pady=10, sticky="e")

def clear_all_frames(btn1, btn2, pizza_item_details_frame, item_details_frame, order_details_frame, pizza_cart, selected_pizza_name, delete_button):
    clear_frame(pizza_item_details_frame)
    clear_frame(item_details_frame)
    clear_cart(order_details_frame, pizza_cart)
    btn1.config(state=tk.NORMAL)
    btn2.config(state=tk.DISABLED)
    selected_pizza_name.set("")
    if delete_button:
        delete_button.config(state=tk.DISABLED)

def clear_cart(order_details_frame, pizza_cart):
    pizza_cart.clear()
    clear_frame(order_details_frame)
    tk.Label(order_details_frame, text="Your cart is empty").grid(row=0, column=0)

def confirm_order(order_details_frame, pizza_cart):
    pizza_cart.clear()
    clear_frame(order_details_frame)
    tk.Label(order_details_frame, text="Order successfully placed!").grid(row=0, column=0)

def add_pizza(allPizzaDict, pizza_prices, pizza_item_details_frame, item_details_frame, order_details_frame, pizza_cart, selected_pizza_name, btn1, btn2, delete_button):
    def save_pizza():
        name = name_entry.get().strip()
        price = price_entry.get().strip()
        if not name or not price or not image_path.get():
            messagebox.showerror("Input Error", "Please fill in all fields and select an image.")
            return

        if name in allPizzaDict:
            messagebox.showerror("Duplicate Name", "A pizza with this name already exists.")
            return

        try:
            price_val = float(price)
        except ValueError:
            messagebox.showerror("Input Error", "Price must be a number.")
            return

        try:
            img = Image.open(image_path.get())
            img_resized = img.resize((80, 80))
            save_path = os.path.join("allPizza", f"{name}.png")
            img.save(save_path)
        except Exception as e:
            messagebox.showerror("Image Save Error", f"Failed to save image: {e}")
            return

        allPizzaDict[name] = ImageTk.PhotoImage(img_resized)
        pizza_prices[name] = price_val

        try:
            with open("pizza_prices.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([name, price_val])
        except Exception as e:
            messagebox.showerror("CSV Save Error", f"Failed to save price to CSV: {e}")
            allPizzaDict.pop(name, None)
            pizza_prices.pop(name, None)
            if os.path.exists(save_path):
                os.remove(save_path)
            return

        pizza_images_as_buttons(btn1, btn2, allPizzaDict, pizza_item_details_frame,
                                item_details_frame, order_details_frame, pizza_cart, pizza_prices, selected_pizza_name, delete_button)
        add_window.destroy()

    add_window = tk.Toplevel()
    add_window.title("Add New Pizza")
    add_window.geometry("350x180")
    add_window.grab_set()

    tk.Label(add_window, text="Pizza Name:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    name_entry = tk.Entry(add_window)
    name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    tk.Label(add_window, text="Pizza Price (£):").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    price_entry = tk.Entry(add_window)
    price_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    image_path = tk.StringVar(value="")

    def select_image():
        filepath = filedialog.askopenfilename(
            title="Select Pizza Image",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.tiff")])
        if filepath:
            image_path.set(filepath)
            image_name_label.config(text=os.path.basename(filepath))

    tk.Button(add_window, text="Select Image", command=select_image).grid(row=2, column=0, columnspan=2, pady=5)
    image_name_label = tk.Label(add_window, text="No image selected", fg="red")
    image_name_label.grid(row=3, column=0, columnspan=2, pady=2)

    tk.Button(add_window, text="Add Pizza", width=15, command=save_pizza).grid(row=4, column=0, columnspan=2, pady=10)

def del_pizza(allPizzaDict, pizza_prices, pizza_item_details_frame, item_details_frame, order_details_frame, pizza_cart, selected_pizza_name, delete_button, btn1, btn2):
    name = selected_pizza_name.get()
    if not name:
        messagebox.showinfo("No Selection", "Please select a pizza to delete")
        return

    if messagebox.askyesno("Confirm Delete", f"Delete '{name}' from menu?"):
        allPizzaDict.pop(name, None)
        pizza_prices.pop(name, None)

        try:
            os.remove(os.path.join("allPizza", f"{name}.png"))
        except FileNotFoundError:
            pass

        try:
            with open("pizza_prices.csv", "w", newline="") as file:
                writer = csv.writer(file)
                for pname, price in pizza_prices.items():
                    writer.writerow([pname, price])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update CSV: {e}")

        clear_frame(item_details_frame)
        clear_cart(order_details_frame, pizza_cart)
        pizza_images_as_buttons(btn1, btn2, allPizzaDict, pizza_item_details_frame,
                                item_details_frame, order_details_frame, pizza_cart, pizza_prices,
                                selected_pizza_name, delete_button)

        selected_pizza_name.set("")
        delete_button.config(state=tk.DISABLED)

def quitApp(myApp):
    if messagebox.askyesno("Confirm Quit", "Are you sure you want to quit?"):
        myApp.quit()

def configure_style():
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 10))
    style.configure("big.TButton", font=("Arial", 12, "bold"))

def create_frames(myApp):
    top_frame = tk.Frame(myApp, height=50, bg="light grey")
    top_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
    top_frame.grid_propagate(False)

    pizza_item_details_frame = tk.Frame(myApp, bg="red", width=600, height=300)
    pizza_item_details_frame.config(width=1200, height=300)
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

def create_buttons(frame, myApp, allPizzaDict, pizza_item_details_frame, item_details_frame, order_details_frame, pizza_cart, pizza_prices):
    selected_pizza_name = tk.StringVar(value="")
    btn1 = ttk.Button(frame, text="Show All Pizzas")
    btn2 = ttk.Button(frame, text="Clear All Pizzas", state=tk.DISABLED)
    delete_button = ttk.Button(frame, text="Delete", state=tk.DISABLED)

    btn1.config(command=lambda:
                pizza_images_as_buttons(btn1, btn2, allPizzaDict, pizza_item_details_frame,
                                        item_details_frame, order_details_frame, pizza_cart,
                                        pizza_prices, selected_pizza_name, delete_button))

    btn2.config(command=lambda:
                clear_all_frames(btn1, btn2, pizza_item_details_frame, item_details_frame,
                                 order_details_frame, pizza_cart, selected_pizza_name, delete_button))

    delete_button.config(command=lambda:
                         del_pizza(allPizzaDict, pizza_prices, pizza_item_details_frame, item_details_frame,
                                   order_details_frame, pizza_cart, selected_pizza_name, delete_button, btn1, btn2))

    btn1.grid(row=0, column=0, padx=5, pady=5)
    btn2.grid(row=0, column=1, padx=5, pady=5)
    delete_button.grid(row=0, column=2, padx=5, pady=5)

    ttk.Button(frame, text="Add New",
               command=lambda:
               add_pizza(allPizzaDict, pizza_prices, pizza_item_details_frame, item_details_frame,
                         order_details_frame, pizza_cart, selected_pizza_name, btn1, btn2, delete_button)).grid(row=0,
                                                                                                             column=3,
                                                                                                             padx=5,
                                                                                                             pady=5)

    ttk.Button(frame, text="Quit", command=lambda: quitApp(myApp)).grid(row=0, column=4, padx=5, pady=5)

def clear_all_frames(btn1, btn2, pizza_item_details_frame, item_details_frame, order_details_frame, pizza_cart, selected_pizza_name, delete_button):
    clear_frame(pizza_item_details_frame)
    clear_frame(item_details_frame)
    clear_cart(order_details_frame, pizza_cart)
    btn1.config(state=tk.NORMAL)
    btn2.config(state=tk.DISABLED)
    selected_pizza_name.set("")
    if delete_button:
        delete_button.config(state=tk.DISABLED)

def main():
    if not os.path.exists("allPizza"):
        os.makedirs("allPizza")

    if not os.path.exists("pizza_prices.csv"):
        with open("pizza_prices.csv", "w", newline="") as file:
            pass

    myApp = tk.Tk()
    myApp.title("Online Pizza Store by Student-w123456")
    myApp.geometry("1200x800")
    configure_style()
    frames = create_frames(myApp)

    pathAllPizza = 'allPizza/'
    pizza_prices_csv = "pizza_prices.csv"

    allPizzaDict, pizza_cart = {}, {}
    pizza_prices = load_pizza_prices(pizza_prices_csv)

    save_images(pathAllPizza, allPizzaDict)
    create_buttons(frames["menu"], myApp, allPizzaDict, frames["pizza"], frames["details"], frames["cart"],
                   pizza_cart, pizza_prices)

    myApp.mainloop()

main()
