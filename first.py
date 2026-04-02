# Simple Finance Dashboard (CLI Version)

balance = 10000

transactions = [
    {"type": "income", "amount": 5000, "category": "Salary"},
    {"type": "expense", "amount": 2000, "category": "Food"},
    {"type": "expense", "amount": 1500, "category": "Transport"},
]

def show_summary():
    income = sum(t["amount"] for t in transactions if t["type"] == "income")
    expense = sum(t["amount"] for t in transactions if t["type"] == "expense")

    print("----- Financial Summary -----")
    print(f"Total Balance: ₹{balance}")
    print(f"Total Income: ₹{income}")
    print(f"Total Expense: ₹{expense}")

def show_transactions():
    print("\n----- Transactions -----")
    for t in transactions:
        print(f"{t['type'].upper()} | ₹{t['amount']} | {t['category']}")

def main():
    show_summary()
    show_transactions()

if __name__ == "__main__":
    main()