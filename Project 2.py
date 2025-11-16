print ("Govinda Mohabir COP1000 11/16/2025")

class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class VendingMachine:
    def __init__(self):
        self.beverages = [
            Beverage("Coke", 1.50),
            Beverage("Pepsi", 1.50),
            Beverage("Water", 1.00),
            Beverage("Orange Juice", 2.00),
            Beverage("Lemonade", 1.75),
            Beverage("Iced Tea", 1.75)
        ]

    def display_beverages(self):
        print("\nAvailable Beverages:")
        for i, beverage in enumerate(self.beverages):
            print(f"{i + 1}. {beverage.name} - ${beverage.price}")

    def select_beverage(self):
        choice = int(input("Select a beverage (1-6): "))
        return choice - 1

    def insert_money(self, price):
        money = float(input("Insert money ($): "))
        return money

    def vend(self, choice, money_inserted):
        if money_inserted >= self.beverages[choice].price:
            change = money_inserted - self.beverages[choice].price
            print(f"Vending {self.beverages[choice].name}. Change: ${change:.2f}\n")
        else:
            print("Insufficient funds. Please insert more money.\n")


def main():
    machine = VendingMachine()

    while True:
        machine.display_beverages()
        choice = machine.select_beverage()
        if choice < 0 or choice >= len(machine.beverages):
            print("Invalid selection. Please try again.")
            continue
        money_inserted = machine.insert_money(machine.beverages[choice].price)
        machine.vend(choice, money_inserted)


if __name__ == "__main__":
    main()