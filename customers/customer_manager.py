import csv

from config import CUSTOMER_FILE
from customers.customer import Customer


class Customer_manager:
    def load_customers(self):
        customers = []
        try:
            with open(CUSTOMER_FILE, "r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    customer = Customer(
                        row["CustomerID"],
                        row["Name"],
                        row["Email"],
                        row["Phone"],
                    )
                    customers.append(customer)
        except FileNotFoundError:
            pass
        return customers

    def save_customers(self, customers):
        with open(CUSTOMER_FILE, "w", newline="") as file:
            fieldnames = [
                "CustomerID",
                "Name",
                "Email",
                "Phone",
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for customer in customers:
                writer.writerow(customer.to_dict())

    def add_customer(self):
        customers = self.load_customers()
        customer_id = input("Enter Customer ID : ")
        for c in customers:
            if c.customer_id == customer_id:
                print("Customer ID already exists.")
                return
        name = input("Enter Customer Name : ")
        email = input("Enter Email : ")
        phone = input("Enter Phone : ")
        new_customer = Customer(customer_id, name, email, phone)
        customers.append(new_customer)
        self.save_customers(customers)
        print("Customer Added Successfully.")

    def view_customers(self):
        customers = self.load_customers()
        if len(customers) == 0:
            print("There are no customers found")
        else:
            for customer in customers:
                customer.display()

    def search_customer(self):
        search_id = input("Enter Customer ID : ")
        customers = self.load_customers()
        for item in customers:
            if item.customer_id == search_id:
                item.display()
                return
        print("Customer Not Found")

    def update_customer(self):
        customers = self.load_customers()
        user_input = input("What Customer would you like to update : ")
        for c in customers:
            if c.customer_id == user_input:
                c.name = input("Enter New Name : ")
                c.email = input("Enter New Email : ")
                c.phone = input("Enter New Phone : ")
                self.save_customers(customers)
                print("Customer Updated Successfully.")
                return

        print("Customer not found")

    def delete_customer(self):
        customers = self.load_customers()
        user_input = input("What customer would you like to remove: ")
        for c in customers:
            if c.customer_id == user_input:
                customers.remove(c)
                self.save_customers(customers)
                print("Customer Removed")
                return
        print("Customer not found")