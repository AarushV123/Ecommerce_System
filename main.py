from config import PROJECT_NAME
from customers.customer_manager import Customer_manager
from products.product_manager import ProductManager


def product_menu(product_manager):
    while True:
        print("\n" + "=" * 50)
        print("PRODUCT MANAGEMENT")
        print("=" * 50)
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Back to Main Menu")
        choice = input("Enter Choice : ")

        if choice == "1":
            product_manager.add_product()
        elif choice == "2":
            product_manager.view_products()
        elif choice == "3":
            product_manager.search_product()
        elif choice == "4":
            product_manager.update_product()
        elif choice == "5":
            product_manager.delete_product()
        elif choice == "6":
            break
        else:
            print("Invalid Choice")


def customer_menu(customer_manager):
    while True:
        print("\n" + "=" * 50)
        print("CUSTOMER MANAGEMENT")
        print("=" * 50)
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Search Customer")
        print("4. Update Customer")
        print("5. Delete Customer")
        print("6. Back to Main Menu")
        choice = input("Enter Choice : ")

        if choice == "1":
            customer_manager.add_customer()
        elif choice == "2":
            customer_manager.view_customers()
        elif choice == "3":
            customer_manager.search_customer()
        elif choice == "4":
            customer_manager.update_customer()
        elif choice == "5":
            customer_manager.delete_customer()
        elif choice == "6":
            break
        else:
            print("Invalid Choice")


def main():
    product_manager = ProductManager()
    customer_manager = Customer_manager()

    while True:
        print("\n" + "=" * 50)
        print(PROJECT_NAME)
        print("=" * 50)
        print("1. Product Management")
        print("2. Customer Management")
        print("3. Exit")
        choice = input("Enter Choice : ")

        if choice == "1":
            product_menu(product_manager)
        elif choice == "2":
            customer_menu(customer_manager)
        elif choice == "3":
            print("Thank You")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()