class Shop:
   def __init__(self, name = None, price = None, stock = None):
     self.name = name
     self.email = price
     self.phone = stock



class IProduct(metaclass=ABC):
     
     @abstractmethod
     def Add(self):
            pass
     @abstractmethod
     def Delete(self):
        pass
     @abstractmethod
     def Edit(self):
        pass
     @abstractmethod
     def List(self):
        pass

class ProductService(ABC):
   
   def __init__(self):
    self.user = []

   def Add(self, product: Product):
        self.user.append(product)

   def Delete(self, id: int):
        del self.user[id]
   
   def Edit(self, id: str, new_product: Product):
        self.user[id] = new_product
        
   def List(self):
        for i, product in enumerate(self.product):
            print(f"Product {i}: {product.name}, {product.price} {product.stock}")

def main():
    productService = ProductService()
    
    while True:
        print("\nOptions:")
        print("1. Add ")
        print("2. Edit ")
        print("3. Delete ")
        print("4. List ")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            name = input("Name: ")
            price = input("Price: ")
            stock = input("Stock: ")
            
            product = Product(name,price,stock)

            productService.Add(product)
            print("Product added.")
            

        elif choice == '2':
            id1 = input("Id: ")
            name = input("Name: ")
            price = input("Price: ")
            stock = input("Stock: ")
            
            product2 = Product(id1,name,price,stock)

            productService.Add(product2)
            print("Product updated.")

        elif choice == '3':
            id2 = int(input("Type product id to delete: "))
            productService.Delete(id2) 
            print("User deleted.")
        
        elif choice == '4':
            print("Products:")
            productService.List()
        
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Option No Valid.")

if __name__ == "__main__":
    main()