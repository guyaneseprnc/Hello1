print ("Govinda Mohabir 12/1/25 COP 1000")

class Airplane:
    def __init__(self):
        self.total_seats = 20
        self.first_class_seats = 5
        self.emergency_rows = [1, 2]
        self.available_seats = set(range(1, self.total_seats + 1))
        self.occupied_seats = set()
        self.first_class_fee = 50

    def display_seats(self):
        print("Available Seats:", sorted(self.available_seats))
        print("Occupied Seats:", sorted(self.occupied_seats))
        print()

    def purchase_seat(self, seat_number, is_first_class):
        if seat_number in self.occupied_seats:
            print("Seat already taken. Please choose another seat.")
            return False

        if seat_number not in self.available_seats:
            print("Invalid seat number. Please choose a valid seat.")
            return False

        if is_first_class:
            self.available_seats.remove(seat_number)
            self.occupied_seats.add(seat_number)
            print(f"You have purchased first-class seat {seat_number} for ${self.first_class_fee}.")
        else:
            self.available_seats.remove(seat_number)
            self.occupied_seats.add(seat_number)
            print(f"You have purchased regular seat {seat_number}.")

        return True

    def purchase_multiple_seats(self, num_seats, is_first_class):
        for _ in range(num_seats):
            seat_number = int(input("Enter seat number: "))
            if seat_number in self.emergency_rows:
                response = input("Are you willing to help in case of an emergency? (yes/no): ").lower()
                if response != "yes":
                    print("You cannot select emergency seats without accepting responsibility.")
                    return

            success = self.purchase_seat(seat_number, is_first_class)
            if not success:
                return

            print()

        print(f"You have successfully purchased {num_seats} seats.")
        print("Thank you for flying with us!\n")


def main():
    airplane = Airplane()

    while True:
        print("1. Purchase First-Class Seat")
        print("2. Purchase Regular Seat")
        print("3. Exit")

        choice = int(input("Enter your choice (1/2/3): "))

        if choice == 1:
            airplane.display_seats()
            num_seats = int(input("Enter the number of first-class seats you want to purchase: "))
            airplane.purchase_multiple_seats(num_seats, is_first_class=True)
        elif choice == 2:
            airplane.display_seats()
            num_seats = int(input("Enter the number of regular seats you want to purchase: "))
            airplane.purchase_multiple_seats(num_seats, is_first_class=False)
        elif choice == 3:
            print("Thank you for using the seat reservation system. Have a great flight!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")


if __name__ == "__main__":
    main()