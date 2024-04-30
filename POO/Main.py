import UserService
import ShoppingCart
import PaymentService
import User
import Payment
import Product

def main():
    shoppingCart = ShoppingCart.ShoppingCart()
    userService = UserService.UserService()
    paymentService = PaymentService.PaymentService()
    

    while True:
        user = User.User("Pacho","78132","pacho@email.com")
        product = Product.Product("ProductoPredeterminado", 1)
        shoppingCart.add(product)
        userService.Add(user)
        print("\nOptions:")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Edit Account")
        print("4. Checkout")
        print("5. Payment")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Name: ")
            price = input("Price: ")
            product2 = Product.Product(name,price)
            shoppingCart.add(product2)

        elif choice == '2':
            shoppingCart.remove(product2)

        elif choice == '3':
            id = 0
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            user2 = User.User(name,phone,email)
            userService.edit(id,user2)

        elif choice == '4':
            print(f"Your total price is: {shoppingCart.checkout(product)}")

        elif choice == '5':
            payment = Payment.Payment(user,product,shoppingCart.checkout(product))
            paymentService.pay(payment)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
