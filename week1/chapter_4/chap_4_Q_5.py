customers = []

def add_customer(name, balance):
    customer = [name, balance]
    customers.append(customer)
    print("Customer added successfully.")

def remove_customer(name):
    for customer in customers:
        if customer[0] == name:
            customers.remove(customer)
            print("Customer removed successfully.")
            return
    print("Customer not found.")

def deposit(name, amount):
    for customer in customers:
        if customer[0] == name:
            customer[1] += amount
            print("Deposit successful.")
            return
    print("Customer not found.")

def withdraw(name, amount):
    for customer in customers:
        if customer[0] == name:
            if customer[1] >= amount:
                customer[1] -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient funds.")
            return
    print("Customer not found.")

def print_balance(name):
    for customer in customers:
        if customer[0] == name:
            print(f"Balance of {customer[0]}'s account: {customer[1]}")
            return
    print("Customer not found.")

def list_customers():
    print("Customer List:")
    for customer in customers:
        print(f"Name: {customer[0]}, Balance: {customer[1]}")

# Main program loop
while True:
    print("\n---- Banking System Menu ----")
    print("1. Add Customer")
    print("2. Remove Customer")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Print Balance")
    print("6. List Customers")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter customer name: ")
        balance = float(input("Enter initial balance: "))
        add_customer(name, balance)

    elif choice == "2":
        name = input("Enter customer name to remove: ")
        remove_customer(name)

    elif choice == "3":
        name = input("Enter customer name: ")
        amount = float(input("Enter deposit amount: "))
        deposit(name, amount)

    elif choice == "4":
        name = input("Enter customer name: ")
        amount = float(input("Enter withdrawal amount: "))
        withdraw(name, amount)

    elif choice == "5":
        name = input("Enter customer name: ")
        print_balance(name)

    elif choice == "6":
        list_customers()

    elif choice == "0":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")