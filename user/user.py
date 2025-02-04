import subprocess
from .db_setup import get_cursor

class User:
    def __init__(self):
        self.web_uid = -1
        self.fname = ""
        self.lname = ""

    def get_unique_web_user_id(self):
        """Fetch a unique Web_User_ID by incrementing the max ID in the table."""
        try:
            conn, cursor = get_cursor()

            query = "SELECT MAX(Web_User_ID) FROM web_user"
            cursor.execute(query)
            result = cursor.fetchone()

            max_id = result[0] if result[0] is not None else 0  # Handle NULL case
            unique_id = int(max_id) + 1

            return unique_id

        except Exception as e:
            print(f"get_unique_web_user_id: Error: {e}")
            return None

    def login(self):
        web_uid1 = input("Enter your web user ID: ")
        password = input("Enter your password: ")
        query = "SELECT password, First_Name, Last_Name FROM web_user WHERE Web_User_ID=%s"

        connection, cursor = get_cursor()
        if cursor:
            try:
                cursor.execute(query, (web_uid1,))
                row = cursor.fetchone()

                if row:
                    db_password, self.fname, self.lname = row
                    if db_password == password:
                        print(f"✅ Logged in successfully! Welcome, {self.fname} {self.lname}!")
                        self.web_uid = web_uid1
                        return True
                    else:
                        print("❌ Login failed: Incorrect password.")
                else:
                    print("❌ Login failed: User ID not found.")

                cursor.close()
                connection.close()
            except Exception as e:
                print(f"❌ Error executing query: {e}")
        else:
            print("❌ Failed to get cursor, check DB connection!")
        return False  # Ensure False is returned when login fails

    def signup(self, wid):
        web_uid = wid
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        email_id = input("Enter your email ID: ")
        age = int(input("Enter your age: "))
        phone_no = input("Enter your phone number: ")
        password = input("Create a password: ")

        check_query = "SELECT COUNT(*) FROM web_user WHERE Web_User_ID = %s"
        insert_query = "INSERT INTO web_user (Web_User_ID, First_Name, Last_Name, Email_ID, Age, Phone_Number, password) VALUES (%s, %s, %s, %s, %s, %s, %s)"

        connection, cursor = get_cursor()
        if cursor:
            try:
                cursor.execute(check_query, (web_uid,))
                count = cursor.fetchone()[0]

                if count > 0:
                    print(f"⚠️ User ID {web_uid} already exists. Please choose a different ID.")
                else:
                    cursor.execute(insert_query, (web_uid, first_name, last_name, email_id, age, phone_no, password))
                    connection.commit()
                    print("✅ Signup successful!")
                    print(f"Your web user ID is: {web_uid}")
            except Exception as e:
                print(f"❌ Error executing query: {e}")
            finally:
                cursor.close()
                connection.close()
        else:
            print("❌ Failed to get cursor, check DB connection!")

u = User()

if __name__ == "__main__":
    u = User()

    while True:
        print("\n1. Login")
        print("2. Sign Up")
        print("3. Exit")

        choice = input("Enter a choice [1-3]: ")

        if choice == "1":
            if u.login():
                with open('userr.py') as file:
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
