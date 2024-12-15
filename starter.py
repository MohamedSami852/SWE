from abc import ABC, abstractmethod

class InventoryManager:
    _inventory = {
        "Margherita": 10,
        "Pepperoni": 10,
        "Cheese": 15,
        "Olives": 10,
        "Mushrooms": 12,
    }

    def check_and_decrement(self, item: str) -> bool:
        if self._inventory.get(item, 0) > 0:
            self._inventory[item] -= 1
            return True
        return False

    def get_inventory(self):
        return self._inventory


class Pizza(ABC):

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod

    def get_cost(self):
        pass


class MargheritaPizza(Pizza):

    def get_description(self):
        return "Margherita Pizza"

    def get_cost(self):
        return 5.0


class PepperoniPizza(Pizza):

    def get_description(self):
        return "Pepperoni Pizza"

    def get_cost(self):
        return 6.0


class PizzaToppings(Pizza):

    def __init__(self, pizza):
        self.pizza = pizza


class Cheese(PizzaToppings):

    def get_description(self):
        return f"{self.pizza.get_description()} + Cheese"

    def get_cost(self):
        return self.pizza.get_cost() + 1.0


class Olives(PizzaToppings):

    def get_description(self):

        return f"{self.pizza.get_description()} + Olives"

    def get_cost(self):
        Olives_price = 0.5
        return self.pizza.get_cost() + Olives_price


class Mushrooms(PizzaToppings):
    def get_description(self):
        return f"{self.pizza.get_description()} + Mushrooms"

    def get_cost(self):
        Mushroom_price = 0.7
        return self.pizza.get_cost() + Mushroom_price


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card.")


class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid ${amount} using PayPal.")


def main():
    inventory_manager = InventoryManager()

    print("Welcome to the Pizza Restaurant!")

    while True:
        
        print("\nChoose your base pizza:")
        print("1. Margherita ($5.0)")
        print("2. Pepperoni ($6.0)")
        print("0. Exit")
        pizza_choice = input("Enter the number of your choice: ")

        if pizza_choice == "0":
            print("Thank you for visiting! Goodbye!")
            break

        if pizza_choice == "1":
            if inventory_manager.check_and_decrement("Margherita"):
                pizza = MargheritaPizza()
            else:
                print("Margherita is out of stock!")
                continue
        elif pizza_choice == "2":
            if inventory_manager.check_and_decrement("Pepperoni"):
                pizza = PepperoniPizza()
            else:
                print("Pepperoni is out of stock!")
                continue
        else:
            print("Invalid choice! Please try again.")
            continue

        while True:
            print("\nAvailable toppings:")
            print("1. Cheese ($1.0)")
            print("2. Olives ($0.5)")
            print("3. Mushrooms ($0.7)")
            print("4. Finish order")
            topping_choice = input("Enter the number of your choice: ")

            if topping_choice == "1":
                if inventory_manager.check_and_decrement("Cheese"):
                    pizza = Cheese(pizza)
                else:
                    print("Cheese is out of stock!")
            elif topping_choice == "2":
                if inventory_manager.check_and_decrement("Olives"):
                    pizza = Olives(pizza)
                else:
                    print("Olives are out of stock!")
            elif topping_choice == "3":
                if inventory_manager.check_and_decrement("Mushrooms"):
                    pizza = Mushrooms(pizza)
                else:
                    print("Mushrooms are out of stock!")
            elif topping_choice == "4":
                break
            else:
                print("Invalid choice! Please try again.")

        print("\nYour order:")
        print(f"Description: {pizza.get_description()}")
        print(f"Total cost: ${pizza.get_cost():.2f}")

        print("\nChoose payment method:")
        print("1. Credit Card")
        print("2. PayPal")
        payment_choice = input("Enter the number of your choice: ")

        if payment_choice == "1":
            payment_method = CreditCardPayment()
        elif payment_choice == "2":
            payment_method = PayPalPayment()
        else:
            print("Invalid payment method! Order canceled.")
            continue

        payment_method.pay(pizza.get_cost())

        print("\nRemaining Inventory:")
        print(inventory_manager.get_inventory())


if __name__ == "__main__":
    main()
