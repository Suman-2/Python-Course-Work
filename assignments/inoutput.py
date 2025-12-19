#int 
atm_pincode=int(input("enter pincode: "))
#string
user_name=input("enter name: ")
bank_name=input("enter bank name: ")
#float 
account_balance=float(input("Enter account balance : "))
withdraw_balance=float(input("Enter withdraw amount : "))
#list
transaction_type=input("enter transaction types: ")
transaction_type=transaction_type.split(",")
#tuple
daily_limit=float(input("enter daily limit: "))
remaining_limit=withdraw_balance-daily_limit
limits=(daily_limit,remaining_limit)
#set 
account_type=input("Enter account_type: ")
account_type=set(account_type.split(","))
#dictionary 
branch_name=input("enter branch name: ")
atm_location=input("enter location: ")
atm_details={
    'branch':branch_name,
    'locate_at':atm_location 
}
print("\n.....details\n")
print(f"pincode is:{atm_pincode}")
print(f"username is:{user_name}")
print(f"bank name is:{bank_name}")
print(f"account_balance is:{account_balance}")
print(f"your withdraw amount is:{withdraw_balance}")
print(f"transaction types available are:{transaction_type}")
print(f"limits are:{limits}")
print(f"account types are:{account_type}")
print(f" atm details are:{atm_details}")