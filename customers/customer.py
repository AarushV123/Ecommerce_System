class Customer:
    def __init__(self, customer_id, name, email, phone):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

    def display(self):
        print(
            f"Customer ID: {self.customer_id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone}"
        )

    def to_dict(self):
        return {
            "CustomerID": self.customer_id,
            "Name": self.name,
            "Email": self.email,
            "Phone": self.phone,
        }