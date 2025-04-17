import uuid
from datetime import datetime

class Account:
    def __init__(self, acc_no, name, gender, mobile, balance, pin):
        self.acc_no = acc_no
        self.name = name
        self.gender = gender
        self.mobile = mobile
        self.balance = balance
        self.pin = pin
        # histories as lists of dicts
        self.deposits = []
        self.withdrawals = []
        self.transfers = []

    def deposit(self, amount, agent):
        tx_id = str(uuid.uuid4())
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.balance += amount
        self.deposits.append({
            'tx_id': tx_id,
            'date': date,
            'mobile': self.mobile,
            'amount': amount,
            'agent': agent
        })
        print(f"[+] Deposit successful: +{amount}. New balance: {self.balance}")

    def withdraw(self, amount, agent):
        if amount > self.balance:
            print("[-] Insufficient funds.")
            return
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.balance -= amount
        self.withdrawals.append({
            'date': date,
            'mobile': self.mobile,
            'amount': amount,
            'agent': agent
        })
        print(f"[+] Withdrawal successful: -{amount}. New balance: {self.balance}")

    def transfer(self, target_acc, amount, agent):
        if amount > self.balance:
            print("[-] Insufficient funds for transfer.")
            return
        tx_id = str(uuid.uuid4())
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.balance -= amount
        target_acc.balance += amount
        self.transfers.append({
            'tx_id': tx_id,
            'date': date,
            'from_mobile': self.mobile,
            'amount': amount,
            'to_acc_no': target_acc.acc_no,
            'agent': agent
        })
        print(f"[+] Transfer successful: -{amount} to {target_acc.acc_no}. New balance: {self.balance}")

    def summary(self):
        print(f"--- Account Summary for {self.acc_no} ---")
        print(f"Name: {self.name} | Gender: {self.gender} | Mobile: {self.mobile}")
        print(f"Balance: {self.balance}")
        print("Deposits:", len(self.deposits), "Withdrawals:", len(self.withdrawals), "Transfers:", len(self.transfers))
        print("-" * 40)


def find_account(accounts, acc_no):
    return next((acc for acc in accounts if acc.acc_no == acc_no), None)

def main():
    accounts = []
    while True:
        print("""
1. Register Account
2. Deposit
3. Withdraw
4. Transfer
5. Show Account Summary
6. Quit
        """)
        choice = input("Choose an option: ").strip()
        if choice == '1':
            acc_no = input("Account No: ")
            if find_account(accounts, acc_no):
                print("[-] Account already exists.")
                continue
            name = input("Holder Name: ")
            gender = input("Gender: ")
            mobile = input("Mobile No: ")
            balance = float(input("Initial Balance: "))
            pin = input("Set PIN: ")
            accounts.append(Account(acc_no, name, gender, mobile, balance, pin))
            print("[+] Account registered.")

        elif choice == '2':
            acc_no = input("Account No: ")
            acc = find_account(accounts, acc_no)
            if not acc:
                print("[-] Account not found.")
                continue
            amt = float(input("Deposit Amount: "))
            agent = input("Agent Name/ID: ")
            acc.deposit(amt, agent)

        elif choice == '3':
            acc_no = input("Account No: ")
            acc = find_account(accounts, acc_no)
            if not acc:
                print("[-] Account not found.")
                continue
            amt = float(input("Withdraw Amount: "))
            agent = input("Agent Name/ID: ")
            acc.withdraw(amt, agent)

        elif choice == '4':
            from_no = input("Your Account No: ")
            acc_from = find_account(accounts, from_no)
            if not acc_from:
                print("[-] Sender account not found.")
                continue
            to_no = input("Receiver Account No: ")
            acc_to = find_account(accounts, to_no)
            if not acc_to:
                print("[-] Receiver account not found.")
                continue
            amt = float(input("Transfer Amount: "))
            agent = input("Agent Name/ID: ")
            acc_from.transfer(acc_to, amt, agent)

        elif choice == '5':
            acc_no = input("Account No: ")
            acc = find_account(accounts, acc_no)
            if not acc:
                print("[-] Account not found.")
                continue
            acc.summary()

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("[-] Invalid choice. Try again.")

if __name__ == "__main__":
    main()
