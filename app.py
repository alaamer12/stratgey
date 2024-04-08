class Customer:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class ReaderStrategy:
    def read(self, file):
        raise NotImplementedError


class CSVReader(ReaderStrategy):
    def read(self, file):
        print(f"Reading data from CSV file: {file}")
        # Implement CSV reading logic here
        pass


class JSONReader(ReaderStrategy):
    def read(self, file):
        print(f"Reading data from JSON file: {file}")
        # Implement JSON reading logic here
        pass


class CustomerDataReader:
    def __init__(self, strategy):
        self.strategy = strategy

    def read(self, file):
        return self.strategy.read(file)


class Invoice:
    def __init__(self, customer, unit, quantity, price):
        self.customer = customer
        self.cart = {"unit": unit, "quantity": quantity}
        self.price = price


# Example usage:
csv_strategy = CSVReader()
json_strategy = JSONReader()

csv_data_reader = CustomerDataReader(csv_strategy)
json_data_reader = CustomerDataReader(json_strategy)

# Now, you can use the appropriate data reader to read customer data from different file formats.
csv_data_reader.read("customer_data.csv")
json_data_reader.read("customer_data.json")
