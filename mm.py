accounts = []
transactions = []

def register_account():
    account = {
        "account_no": int(input("Enter account number: ")),
        "holder_name": input("Enter holder name: "),
        "gender": input("Enter gender: "),
        "mobile_number": int(input("Enter mobile number: ")),
        "balance": float(input("Enter initial balance: ")),
        "pin": int(input("Enter Pin: "))
    }
    accounts.append(account)
    

def find_account_by_mobile(mobile):
    for account in accounts:
        if account == mobile:
            mobile == account
    return None

def record_deposit():
    mobile = input("Enter Mobile Number: ")
    account = find_account_by_mobile(mobile)
    if account:
        amount = float(input("Enter Deposit amount: "))
        transaction = {
            "transaction_id": input("Enter transaction ID: "),
            "date": input("Enter date: "),
            "mobile_number": mobile,
            "amount": amount,
            "agent": input("Enter agent name: ")
        }
        account["balance"] += amount
        transactions.append(transaction)
        print("Deposit successfull!")
    else:
        print("Deposit Unsuccessful!")


def record_withdraw():
    mobile = input("Enter Mobile Number: ")
    account = find_account_by_mobile(mobile)
    if account:
        amount = float(input("Enter withdraw amount: "))
        if account["balance"] >= amount:
            transaction = {
                "transaction_id": input("Enter Transaction ID: "),
                "withdraw_date": input("Enter Withdraw Date: "),
                "mobile_number": mobile,
                "deposit_amount": amount,
                "agent": input("Enter agent name: ")
            }
            account["balance"] -= amount
            transactions.append(transaction)
            print("withdraw successful!")
        else:
            print("Insufficient balance!")
    else:
        print("Account not found!")


def transfer_money():
    sender_mobile = input("Enter sender mobile number: ")
    receiver_mobile = input("Enter Receiver Mobile Number: ")
    sender = find_account_by_mobile(sender_mobile)
    receiver = find_account_by_mobile(receiver_mobile)
    if sender and receiver:
        amount = float(input("Enter amount to transfer: "))
        if sender["balance"] >=amount:
            transaction = {
                "transaction_id": input("Enter transaction ID: "),
                "transfer_date": input("Enter transfer date: "),
                "sender": sender_mobile,
                "amount": amount,
                "receiver": amount
            }
            sender["balance"] -= amount
            receiver["balance"] += amount
            transactions.append(transaction)
            print("transfer successful!")
        else:
            print("Insufficient balance!")
    else:
        print("sender or receiver account not found!")        

        

