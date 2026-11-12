import re

class Validator:
    @staticmethod
    def validate_positive_float(prompt_text):
        """Ensures user inputs a valid positive floating-point number (e.g., Price, Amount)."""
        while True:
            try:
                value = float(input(prompt_text))
                if value < 0:
                    print("Error: Value cannot be negative. Please try again.")
                    continue
                return value
            except ValueError:
                print("Error: Invalid input. Please enter a numerical value.")

    @staticmethod
    def validate_positive_int(prompt_text):
        """Ensures user inputs a valid positive integer (e.g., Stock, Quantity)."""
        while True:
            try:
                value = int(input(prompt_text))
                if value < 0:
                    print("Error: Quantity cannot be negative. Please try again.")
                    continue
                return value
            except ValueError:
                print("Error: Invalid input. Please enter a whole number.")

    @staticmethod
    def validate_email(email):
        """Validates basic email format structure."""
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if re.match(pattern, email):
            return True
        return False

    @staticmethod
    def validate_phone(phone):
        """Validates that phone contains 10 digits."""
        clean_phone = re.sub(r"\D", "", phone)
        if len(clean_phone) >= 10:
            return True
        return False

    @staticmethod
    def safe_input_string(prompt_text):
        """Ensures user provides a non-empty text input string."""
        while True:
            value = input(prompt_text).strip()
            if not value:
                print("Error: Input cannot be empty. Please try again.")
                continue
            return value
