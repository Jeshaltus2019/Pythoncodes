PASSWORD='12345@'
account_balance = 60000
password = input("Enter the password:  ")
tries = 3
while password != PASSWORD:
  if tries > 0:
    tries -=1
    password = input("Incorrect pin re Enter! ")
  else:
      print ("Account blocked.Wrong password! ):")
      exit()
print ("Welcome (:")
user_choice = int(input(''' Select Option 1. Withdraw 2. Deposit 3. View Balance'''))
if user_choice == 1:
    amount = int(input("Enter Amount you want to Widthraw"))
    if amount > account_balance:
        print("Incorrect")
    else:
        account_balance -= amount
    print (account_balance)
elif user_choice == 2:
    amount = int(input("Enter amount you want to deposit: "))
    account_balance += amount
    print (account_balance)
elif user_choice == 3:
    print (account_balance)
else:
    print("Incorrect input!Hope you had a nice time at the ATM!How would you rate your visit?")
    input("Enter the rating: ")