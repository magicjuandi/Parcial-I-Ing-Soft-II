import PersonaService
import Process
import PaymentService
import Persona
import Payment
import Product

def main():
    process = Process.Process()
    personaService = PersonaService.PersonaService()
    paymentService = PaymentService.PaymentService()
    

    while True:
        persona = Persona.Persona("Juana","123812","juana@mail.com")
        product = Product.Product("Producto1", 213)
        process.add(product)
        personaService.Add(persona)
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
            process.add(product2)

        elif choice == '2':
            process.remove(product2)

        elif choice == '3':
            id = 0
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            persona2 = Persona.Persona(name,phone,email)
            personaService.edit(id,persona2)

        elif choice == '4':
            print(f"Your total price is: {process.checkout(product)}")

        elif choice == '5':
            payment = Payment.Payment(persona,product,process.checkout(product))
            paymentService.pay(payment)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
