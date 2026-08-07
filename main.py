from config import PROJECT_NAME
from products.product_manager import ProductManager


def main():
    print("=" * 50)
    print(PROJECT_NAME)
    print("=" * 50)
    print("Welcome to the E-Commerce Sales & Analytics System")
    manager = ProductManager()
    while True:
        print("\n")
        print("=" * 50)
        print(PROJECT_NAME)
        print("=" * 50)
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Exit")
        choice = input("Enter Choice : ")
        if choice == "1":
            manager.add_product()
        elif choice == "2":
            manager.view_products()
        elif choice == "3":
            manager.search_product()
        elif choice == "4":
            manager.update_product()
        elif choice == "5":
            manager.delete_product()
        elif choice == "6":
            print("Thank You")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()