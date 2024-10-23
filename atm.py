# ATM BASIC OPRATIONS 

import time

print("Please insert Your CARD")

time.sleep(5)

password = 4321 
# USER ENTER THE ATM  PIN 
pin = int(input("enter your atm pin : "))   

balance = 10000

if pin == password:

    while True :
        # OPERATION OPTION
        print(""""
            1 == balance
            2 == withdraw balance
            3 == deposit balance
            4 == exit
            """
            )
        # EXCEPTION HANDLE
        try:
            option = int(input("Please enter your choise : "))

        except:
            print("Please enter valid option")
            
        # BALANCE ENQUIRY

        if option == 1:
            print(f"Your current balance is {balance}")
            print("********************Program Execute *********************")

        # WITHDRAW OPERATION

        if option == 2:
            withdraw_amount = int(input("Please enter withdraw_amount : " ))
            balance = balance - withdraw_amount
            print(f"{withdraw_amount} is debited from your account")
            print(f"your updated balance is {balance}")
            print("***************** Program Execute ************************")

        # DEPOSIT OPERATION 

        if option == 3:
            deposit_amount = int(input("Please enter deposit_amount : "))
            balance = balance + deposit_amount
            print(f"{deposit_amount} is credited to your account.")
            print(f"your updated balance is {balance}")
            print("******************* Program Execute **********************")

        # WHILE LOOP EXIT OPERATION

        if option == 4:
            break

else:
    print("wrong pin Please try again")
    print("******************* Program Execute **********************")
