class POS:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity, price):
        if quantity <= 0 or price < 0:
            print("Quantity must be > 0 and price >= 0.")
            return
        self.items.append({'name': name, 'qty': quantity, 'price': price})

    def calculate_total(self):
        return sum(item['qty'] * item['price'] for item in self.items)

    def print_receipt(self):
        print("\n===== Receipt =====")
        print(f"{'Item':20} {'Qty':>5} {'Price':>10} {'Total':>10}")
        print("-" * 50)
        for item in self.items:
            total_price = item['qty'] * item['price']
            print(f"{item['name']:20} {item['qty']:>5} {item['price']:>10.2f} {total_price:>10.2f}")
        print("-" * 50)
        total = self.calculate_total()
        print(f"{'Total Bill':>37} : ${total:.2f}")
        print("===================\n")

def main():
    pos = POS()
    print("Welcome to Mini POS Billing System")
    while True:
        name = input("Enter item name (or 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
        try:
            qty = int(input("Enter quantity: "))
            price = float(input("Enter price per item: "))
        except ValueError:
            print("Invalid input. Quantity must be integer and price must be a number.")
            continue

        pos.add_item(name, qty, price)

    pos.print_receipt()

if __name__ == "__main__":
    main()
