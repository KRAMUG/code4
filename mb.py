import random
from datetime import datetime

# Global variables to store data
accounts = {}
deposits = []
withdrawals = []
transfers = []
transaction_id_counter = 1000

def generate_account_number():
    return str(random.randint(1000000000, 9999999999))

def generate_transaction_id():
    global transaction_id_counter
    transaction_id_counter += 1
    return f"TX{transaction_id_counter}"

def register_account():
    print("\n--- Create New Account ---")
    
    # Get user input
    name = input("Enter your full name: ")
    gender = input("Enter gender (M/F/O): ").upper()
    while gender not in ['M', 'F', 'O']:
        gender = input("Invalid input. Enter gender (M/F/O): ").upper()
    
    mobile = input("Enter mobile number: ")
    while not mobile.isdigit() or len(mobile) < 10:
        mobile = input("Invalid number. Enter 10+ digit mobile number: ")
    
    initial_deposit = float(input("Enter initial deposit amount: "))
    while initial_deposit < 0:
        initial_deposit = float(input("Amount cannot be negative. Enter initial deposit: "))
    
    pin = input("Create 4-digit PIN: ")
    while len(pin) != 4 or not pin.isdigit():
        pin = input("PIN must be 4 digits. Create PIN: ")
    
    # Create account
    account_number = generate_account_number()
    accounts[account_number] = {
        'name': name,
        'gender': gender,
        'mobile': mobile,
        'balance': initial_deposit,
        'pin': pin
    }
    
    # Record initial deposit
    record_deposit(account_number, initial_deposit, "Self", "New Account")
    
    print(f"\nAccount created successfully!")
    print(f"Account Number: {account_number}")
    print(f"Name: {name}")
    print(f"Balance: {initial_deposit:.2f}")

def record_deposit(account_number, amount, agent, deposited_by):
    transaction_id = generate_transaction_id()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    deposits.append({
        'transaction_id': transaction_id,
        'date': timestamp,
        'account_number': account_number,
        'amount': amount,
        'agent': agent,
        'deposited_by': deposited_by
    })
    
    # Update account balance
    accounts[account_number]['balance'] += amount
    
    print(f"\nDeposit successful! Transaction ID: {transaction_id}")
    print(f"New balance: {accounts[account_number]['balance']:.2f}")

def record_withdrawal(account_number, amount):
    if accounts[account_number]['balance'] < amount:
        print("Insufficient funds!")
        return
    
    transaction_id = generate_transaction_id()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    withdrawals.append({
        'transaction_id': transaction_id,
        'date': timestamp,
        'account_number': account_number,
        'amount': amount
    })
    
    # Update account balance
    accounts[account_number]['balance'] -= amount
    
    print(f"\nWithdrawal successful! Transaction ID: {transaction_id}")
    print(f"New balance: {accounts[account_number]['balance']:.2f}")

def record_transfer(sender_account, receiver_account, amount):
    if sender_account not in accounts or receiver_account not in accounts:
        print("Invalid account number(s)")
        return
    
    if accounts[sender_account]['balance'] < amount:
        print("Insufficient funds!")
        return
    
    transaction_id = generate_transaction_id()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    transfers.append({
        'transaction_id': transaction_id,
        'date': timestamp,
        'sender_account': sender_account,
        'receiver_account': receiver_account,
        'amount': amount
    })
    
    # Update balances
    accounts[sender_account]['balance'] -= amount
    accounts[receiver_account]['balance'] += amount
    
    print(f"\nTransfer successful! Transaction ID: {transaction_id}")
    print(f"Sender new balance: {accounts[sender_account]['balance']:.2f}")

def login():
    account_number = input("Enter account number: ")
    pin = input("Enter PIN: ")
    
    if account_number in accounts and accounts[account_number]['pin'] == pin:
        return account_number
    else:
        print("Invalid account number or PIN")
        return None

def main_menu():
    while True:
        print("\n=== Mobile Money System ===")
        print("1. Register New Account")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Select option: ")
        
        if choice == '1':
            register_account()
        elif choice == '2':
            account_number = login()
            if account_number:
                account_menu(account_number)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

def account_menu(account_number):
    while True:
        print(f"\nWelcome, {accounts[account_number]['name']}")
        print(f"Balance: {accounts[account_number]['balance']:.2f}")
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. View Transactions")
        print("5. Logout")
        
        choice = input("Select option: ")
        
        if choice == '1':
            amount = float(input("Enter deposit amount: "))
            agent = input("Enter agent name: ")
            deposited_by = input("Deposited by (your name): ")
            record_deposit(account_number, amount, agent, deposited_by)
        elif choice == '2':
            amount = float(input("Enter withdrawal amount: "))
            record_withdrawal(account_number, amount)
        elif choice == '3':
            receiver = input("Enter receiver account number: ")
            amount = float(input("Enter transfer amount: "))
            record_transfer(account_number, receiver, amount)
        elif choice == '4':
            view_transactions(account_number)
        elif choice == '5':
            break
        else:
            print("Invalid choice")

def view_transactions(account_number):
    print("\n=== Your Transactions ===")
    
    print("\nDeposits:")
    for deposit in deposits:
        if deposit['account_number'] == account_number:
            print(f"{deposit['date']} - ID: {deposit['transaction_id']} - Amount: {deposit['amount']:.2f}")
    
    print("\nWithdrawals:")
    for withdrawal in withdrawals:
        if withdrawal['account_number'] == account_number:
            print(f"{withdrawal['date']} - ID: {withdrawal['transaction_id']} - Amount: {withdrawal['amount']:.2f}")
    
    print("\nTransfers Sent:")
    for transfer in transfers:
        if transfer['sender_account'] == account_number:
            print(f"{transfer['date']} - ID: {transfer['transaction_id']} - Amount: {transfer['amount']:.2f} to {transfer['receiver_account']}")
    
    print("\nTransfers Received:")
    for transfer in transfers:
        if transfer['receiver_account'] == account_number:
            print(f"{transfer['date']} - ID: {transfer['transaction_id']} - Amount: {transfer['amount']:.2f} from {transfer['sender_account']}")

# Start the program
if __name__ == "__main__":
    main_menu()