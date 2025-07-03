def tip_splitter():
    try:
        total_bill = float(input("Enter the total bill amount: $"))
        if total_bill < 0:
            print("Total bill cannot be negative.")
            return

        tip_percent = float(input("Enter the tip percentage (e.g., 15 for 15%): "))
        if tip_percent < 0:
            print("Tip percentage cannot be negative.")
            return

        num_people = int(input("Enter the number of people to split the bill: "))
        if num_people <= 0:
            print("Number of people must be at least 1.")
            return

        tip_amount = total_bill * (tip_percent / 100)
        total_with_tip = total_bill + tip_amount
        amount_per_person = total_with_tip / num_people

        print(f"\nTip amount: ${tip_amount:.2f}")
        print(f"Total amount with tip: ${total_with_tip:.2f}")
        print(f"Each person should pay: ${amount_per_person:.2f}")

    except ValueError:
        print("Please enter valid numerical inputs.")

if __name__ == "__main__":
    tip_splitter()
