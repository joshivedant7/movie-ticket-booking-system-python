from admin.admin import Admin
from user.user import User
import os
import sys
import time

ascii = """ 
    \u001B[34m███╗   ███╗ ██████╗ ██╗   ██╗██╗███████╗    ████████╗██╗ ██████╗██╗  ██╗███████╗████████╗
    ████╗ ████║██╔═══██╗██║   ██║██║██╔════╝    ╚══██╔══╝██║██╔════╝██║ ██╔╝██╔════╝╚══██╔══╝
    ██╔████╔██║██║   ██║██║   ██║██║█████╗         ██║   ██║██║     █████╔╝ █████╗     ██║   
    ██║╚██╔╝██║██║   ██║╚██╗ ██╔╝██║██╔══╝         ██║   ██║██║     ██╔═██╗ ██╔══╝     ██║   
    ██║ ╚═╝ ██║╚██████╔╝ ╚████╔╝ ██║███████╗       ██║   ██║╚██████╗██║  ██╗███████╗   ██║   
    ╚═╝     ╚═╝ ╚═════╝   ╚═══╝  ╚═╝╚══════╝       ╚═╝   ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝   
    \u001B[33m                ██████╗  ██████╗  ██████╗ ██╗  ██╗██╗███╗   ██╗ ██████╗                  
                    ██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝██║████╗  ██║██╔════╝                  
                    ██████╔╝██║   ██║██║   ██║█████╔╝ ██║██╔██╗ ██║██║  ███╗                 
                    ██╔══██╗██║   ██║██║   ██║██╔═██╗ ██║██║╚██╗██║██║   ██║                 
                    ██████╔╝╚██████╔╝╚██████╔╝██║  ██╗██║██║ ╚████║╚██████╔╝                 
                    ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝           \u001B[0m       
"""
print("---------------------------------------------------------------------------------------------------------")
for char in ascii:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.002)
print("---------------------------------------------------------------------------------------------------------")

while True:
    print()
    print("\t\t\t1. for Admin")
    print("\t\t\t2. for User")
    print("\t\t\t3. for Exit")
    print()
    n = input("\t\t\tEnter a choicecls [1-3] : ")

    if n == "1":
        Admin()

    elif n == "2":
        u = User()
        while True:
            print("\n1. Login")
            print("2. Sign Up")
            print("3. Exit")

            choice = input("Enter a choice [1-3]: ")

            if choice == "1":
                if u.login():
                    path = r'C:\Users\HP\OneDrive\Documents\GithubUploads\movie-ticket-booking-system-python\user\userr.py'
                    with open(path) as file:
                        exec(file.read())  

            elif choice == "2":
                wid = u.get_unique_web_user_id()
                if wid is not None:
                    u.signup(wid)
                else:
                    print("❌ Failed to generate a unique Web User ID.")
            elif choice == "3":
                print("🚪 Exiting the program. Goodbye!")
                break
            else:
                print("⚠️ Invalid choice. Please enter a valid option.")

    elif n == "3":
        break
    else:
        print("Enter a valid choice")