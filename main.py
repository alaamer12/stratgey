from abc import ABC, abstractmethod


# Define the Strategy interface
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, amount: float) -> float:
        pass


# Define Concrete Strategy classes
class NoDiscount(DiscountStrategy):
    def apply_discount(self, amount: float) -> float:
        return amount


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float):
        self.percentage = percentage

    def apply_discount(self, amount: float) -> float:
        return amount * (1 - self.percentage / 100)


class FixedDiscount(DiscountStrategy):
    def __init__(self, discount_amount: float):
        self.discount_amount = discount_amount

    def apply_discount(self, amount: float) -> float:
        return amount - self.discount_amount


# Context class
class ShoppingCart:
    def __init__(self, discount_strategy: DiscountStrategy):
        self.discount_strategy = discount_strategy
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def calculate_total_amount(self) -> float:
        total_amount = sum(self.items)
        return total_amount

    def apply_discount(self) -> float:
        total_amount = self.calculate_total_amount()
        return self.discount_strategy.apply_discount(total_amount)


# Example usage
if __name__ == "__main__":
    items = [100, 200, 300]

    # No discount
    no_discount = NoDiscount()
    cart_no_discount = ShoppingCart(no_discount)
    for item in items:
        cart_no_discount.add_item(item)
    print(f"Total amount without discount: {cart_no_discount.calculate_total_amount()}")
    print(f"Final amount after applying no discount: {cart_no_discount.apply_discount()}")

    # Percentage discount
    percentage_discount = PercentageDiscount(10)
    cart_percentage_discount = ShoppingCart(percentage_discount)
    for item in items:
        cart_percentage_discount.add_item(item)
    print(f"Total amount without discount: {cart_percentage_discount.calculate_total_amount()}")
    print(f"Final amount after applying percentage discount: {cart_percentage_discount.apply_discount()}")

    # Fixed discount
    fixed_discount = FixedDiscount(50)
    cart_fixed_discount = ShoppingCart(fixed_discount)
    for item in items:
        cart_fixed_discount.add_item(item)
    print(f"Total amount without discount: {cart_fixed_discount.calculate_total_amount()}")
    print(f"Final amount after applying fixed discount: {cart_fixed_discount.apply_discount()}")
