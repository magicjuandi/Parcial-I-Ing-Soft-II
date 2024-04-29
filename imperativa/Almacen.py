class Product:
    def __init__(self, name=None, price=None, stock=None):
        self.name = name
        self.price = price
        self.stock = stock

def add(products, name, price, stock):
    product = Product(name, price, stock)
    products.append(product)
    print("Product added.")

def edit(products, id, name, price, stock):
    if 0 <= id < len(products):
        products[id].name = name
        products[id].price = price
        products[id].stock = stock
        print("Product updated.")
    else:
        print("Invalid product ID.")

def delete(products, id):
    if 0 <= id < len(products):
        del products[id]
        print("Product deleted.")
    else:
        print("Invalid product ID.")

def list(products):
    for i, product in enumerate(products):
        print(f"Product {i}= name:{product.name}, price:{product.price}, stock:{product.stock}")

def main():
    products = []

    while True:
        print("\nOptions:")
        print("1. Add")
        print("2. Edit")
        print("3. Delete")
        print("4. List")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            name = input("Name: ")
            price = input("Price: ")
            stock = input("Stock: ")
            add(products, name, price, stock)

        elif choice == '2':
            id = int(input("Product ID: "))
            name = input("Name: ")
            price = input("Price: ")
            stock = input("Stock: ")
            edit(products, id, name, price, stock)

        elif choice == '3':
            id = int(input("Product ID to delete: "))
            delete(products, id)

        elif choice == '4':
            print("Products:")
            list(products)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
