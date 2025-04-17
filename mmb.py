
accounts = {}
transactions = []

def main():
    while True:
        print("\nMobile Money System💲")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            print("DEAR CUSTOMER! THANK U FOR USING OUR SERVICES🙂")
            break
        else:
            print("Invalid choice. Please try again.")

def create_account():
    print("\nCreate New Account")
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    
    account_number = phone
    
    if account_number in accounts:
        print("An account already exists with this phone number!Please try again")
        return
    
    pin = input("Create a 4-digit PIN: ")
    while len(pin) != 4 or not pin.isdigit():
        pin = input("PIN must be 4 digits. Try again: ")
    
    accounts[account_number] = {
        "name": name,
        "balance": 0,
        "pin": pin
    }
    
    print(f"\nAccount created successfully!Thank you")
    print(f"Account Number: {account_number}")
    print(f"Name: {name}")

def deposit():
    print("\nDeposit Money")
    account_number = input("Enter account number: ")
    amount = float(input("Enter amount to deposit: "))
    
    if account_number not in accounts:
        print("Account not found!")
        return
    
    accounts[account_number]["balance"] += amount
    transactions.append(f"Deposit: {account_number} +{amount}")
    
    print(f"Deposit successful! New balance: {accounts[account_number]['balance']:.2f}")

def withdraw():
    print("\nWithdraw Money")
    account_number = input("Enter account number: ")
    pin = input("Enter your PIN: ")
    amount = float(input("Enter amount to withdraw: "))
    
    if account_number not in accounts:
        print("Account not found!")
        return
    
    if accounts[account_number]["pin"] != pin:
        print("Wrong PIN!")
        return
    
    if accounts[account_number]["balance"] < amount:
        print("Little money on your account!")
        return
    
    accounts[account_number]["balance"] -= amount
    transactions.append(f"Withdrawal: {account_number} -{amount}")
    
    print(f"Withdrawal successful! New balance: {accounts[account_number]['balance']:.2f}")

def check_balance():
    print("\nCheck Balance")
    account_number = input("Enter account number: ")
    pin = input("Enter your PIN: ")
    
    if account_number not in accounts:
        print("Account not found!")
        return
    
    if accounts[account_number]["pin"] != pin:
        print("Wrong PIN!")
        return
    
    print(f"\nAccount owner: {accounts[account_number]['name']}")
    print(f"Current Balance: {accounts[account_number]['balance']:.2f}")

if __name__ == "__main__":
    main()