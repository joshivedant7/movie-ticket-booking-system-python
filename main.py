from admin.admin import Admin
from user.user import User

print("---------------------------------------------------------------------------------------------------------")
print("                                      WELCOME TO MOVIE TICKET BOOKING                                    ")
print("---------------------------------------------------------------------------------------------------------")


while True:
    print()
    print("1. for Admin")
    print("2. for User")
    print("3. for Exit")
    print()
    n = input("Enter a choicecls [1-3] : ")

    if n == "1":
        Admin()

    elif n == "2":
        User()
    elif n == "3":
        break
    else:
        print("Enter a valid choice")