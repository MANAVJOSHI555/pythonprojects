import os

DATABASE = "accounts.txt"

def create_account():
    print("\n--- Create Account ---")
    name = input("Enter account holder name: ")
    acc_num = input("Enter account number: ")
    acc_type = input("Enter account type (Savings/Current): ")
    balance = float(input("Enter initial deposit: "))
    
    with open(DATABASE, "a") as file:
        file.write(f"{acc_num},{name},{acc_type},{balance}\n")
    print("Account created successfully!\n")

def deposit():
    print("\n--- Deposit Money ---")
    acc_num = input("Enter account number: ")
    amount = float(input("Enter amount to deposit: "))
    
    accounts = []
    found = False
    with open(DATABASE, "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == acc_num:
                data[3] = str(float(data[3]) + amount)
                found = True
            accounts.append(data)
    
    if found:
        with open(DATABASE, "w") as file:
            for acc in accounts:
                file.write(",".join(acc) + "\n")
        print("Amount deposited successfully!\n")
    else:
        print("Account not found.\n")

def withdraw():
    print("\n--- Withdraw Money ---")
    acc_num = input("Enter account number: ")
    amount = float(input("Enter amount to withdraw: "))
    
    accounts = []
    found = False
    with open(DATABASE, "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == acc_num:
                if float(data[3]) >= amount:
                    data[3] = str(float(data[3]) - amount)
                    found = True
                else:
                    print("Insufficient balance.\n")
                    return
            accounts.append(data)
    
    if found:
        with open(DATABASE, "w") as file:
            for acc in accounts:
                file.write(",".join(acc) + "\n")
        print("Amount withdrawn successfully!\n")
    else:
        print("Account not found.\n")

def check_balance():
    print("\n--- Check Balance ---")
    acc_num = input("Enter account number: ")
    
    with open(DATABASE, "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == acc_num:
                print(f"Account Holder: {data[1]}")
                print(f"Account Type: {data[2]}")
                print(f"Balance: {data[3]}")
                return
    print("Account not found.\n")

def main():
    while True:
        print("----- Bank Management System -----")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            print("Thank you for using the Bank Management System!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    if not os.path.exists(DATABASE):
        open(DATABASE, "w").close()  # Create database file if it doesn't exist
    main()
