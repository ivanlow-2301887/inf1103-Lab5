import json
import os

file_name = "inventory.json"
INVENTORY_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)

def load_inventory(filename=INVENTORY_FILE):
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                inventory = json.load(file)
            print(f"{file_name} found. Inventory loaded successfully.")
            return inventory
        except (json.JSONDecodeError, OSError) as error:
            print(f"Error loading {filename}: {error}")
            print("Starting with an empty inventory.")
            return []
    else:
        print(f"{filename} not found. Starting with an empty inventory.")
        return []

def save_inventory(inventory, filename=INVENTORY_FILE):
    print("Saving inventory...")
    try:
        with open(filename, "w") as file:
            json.dump(inventory, file, indent=4)
        print(f"Inventory saved successfully to {filename}.")
    except OSError as error:
        print(f"Error saving inventory: {error}")

def display_all(inventory):
    print("\nCurrent Inventory")
    if not inventory:
        print("No products in inventory.")
        return
    for product in inventory:
        print(f"ID: {product['id']} | Name: {product['name']} | Price: ${product['price']:.2f} | Stock: {product['stock']}")

def add_product(inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ").strip()
    if any(p['id'].lower() == product_id.lower() for p in inventory):
        print("Product ID already exists.")
        return
    name = input("Product Name: ").strip()
    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
    except ValueError:
        print("Invalid price or stock quantity. Product not added.")
        return
    inventory.append({"id": product_id, "name": name, "price": price, "stock": stock})
    print("Product added successfully!")

def update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ").strip()
    for product in inventory:
        if product['id'].lower() == product_id.lower():
            print(f"\nProduct Found:")
            print(f"Name: {product['name']}")
            print(f"Current Stock: {product['stock']}")
            
            try:
                new_stock = int(input("\nNew Stock Quantity: "))
            except ValueError:
                print("Invalid stock quantity.")
                return
            product['stock'] = new_stock
            print("Stock updated successfully!")
            return
    print("Product not found.")

def search_product(inventory):
    print("\nSearch Product")
    product_id = input("Enter Product ID: ").strip()
    for product in inventory:
        if product['id'].lower() == product_id.lower():
            print("\nProduct Found")
            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: ${product['price']:.2f}")
            print(f"Stock: {product['stock']}")
            return
    print("Product not found.")

def main():

    print("\n===================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("===================================")

    inventory = load_inventory()

    while True:
        print("\n---------MENU---------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("----------------------")
        option = input("Enter option: ").strip()

        if option == "1":
            display_all(inventory)
        elif option == "2":
            add_product(inventory)
        elif option == "3":
            update_stock(inventory)
        elif option == "4":
            search_product(inventory)
        elif option == "5":
            save_inventory(inventory)
        elif option == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Thank you for using Inventory Management System. Program terminated.")
            break
        else:
            print("Invalid option. Please choose 1-5.")

if __name__ == "__main__":
    main()