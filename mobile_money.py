# a program to do mobile money transactions 
accounts=[]
transactions=[]

def register_accounts():
    print("\n------REGISTER ACCOUNT------")
    account={
        "account_no":input("enter account number:"),
        "holder_name":input("enter holders name:"),
        "gender":input("enter grnder:"),
        "moblie_no":input("enter mobile number:"),
        "balance":float(input("enter initial balance:")),
        "pin":input("Set PIN:"),
    }
    accounts.append(account)
    print("account registered successfully!")
    def find_account_by_mobile(mobile):
        for account in accounts:
            if account["mobile_number"]==mobile:
                return account
        return None

    def record_deposit():
        print("\n------RECORD DEPOSIT-----")
        mobile=input("enter mobile number:")
        account =find_account_by_mobile(mobile)
        if account:
            amount=float(input("enter deposit amount:"))
            transaction={
                "type":"deposit",
                "transaction_id":input("enter Transaction ID:"),
                "date":input("enter deposit date:"),
                "mobile_number":mobile,
                "amount":amount,
                "agent":input("enter agent name:"),
            }
            account("balance") += amount
        transactions.append(transaction)
        print("deposit successfull!")
        else:
         print("account not found!")
    def record_withdraw():
        print("\n-----Record Withdraw-----")
        mobile=input("enter mobile number:")
        account=find_account_by_mobile(mobile)
        if account:
            amount=float(input("enter withdraw amount:"))
            if account("balance")>=amount:
                transactions={
                    "type":"withdraw",
                    "transaction_id":input("enter transaction ID:"),
                    "date":input("enter withdraw date:"),
                    "mobile_number":mobile,
                    "agent":input("enter agent name:")
                }
                account("balance")-=amount
    transactions.append(transaction)
print("withdraw successful!")
else:
    print("insufficient balance!")

    def transfer_money():
        print("\n-----TRANSFER MONEY-----")
        sender_moblie=input("enter sender's mobile number:") 
        receiver_mobile=input("enter receiver's mobile number:")
        sender=find_account_by_mobile(sender_moblie)
        receiver=find_account_by_mobile(receiver_mobile)
        if sender and receiver:
            amount=float(input("enter amount to transfer:"))
            if sender["balance"]>=amount:
                transaction={
                    "type":"transfer",
                    "transaction_ID":input("Enter Transaction ID"),
                    "date":input("Enter Transfer Date:"),
                    "sender":sender_moblie,
                    "receiver":receiver_mobile,
                    "amount":amount,
                }
                sender("balance") -=amount
                receiver("balance") +=amount

        transactions.append(transaction) 
    print("Insufficient balance!")           
        else:
    print("Sender or Receiver account not found!")

    def main():
        while True:
            print("\n-----Mobile Money Menu-----")
            print("1.Register Account")
            print("2.Record Deposit")
            print("3.Record_Withdraw")
            print("4.Transfer Money")
            print("5.Exit")
            choice=input("choose an option:")
            if choice=="1":
                register_accounts()
            elif choice=="2":
                record_deposit()
            elif choice=="3":
                record_withdraw()
            elif choice=="4":
                transfer_money()
            elif choice=="5":
                print("Exiting system thank you!")
                break
            else:
                print("invalid option, Try again.")