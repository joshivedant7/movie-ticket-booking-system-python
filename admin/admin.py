from .admin_base import AdminBase
from .mange_booking import ManageBooking
from .manage_screen import ManageScreen
from .manage_show import ManageShow
from .manage_movie import ManageMovie
import  mysql.connector

class Admin(AdminBase):
    def __init__(self):
        if super().__init__():
            self.admin_menu()
        else: return

    def admin_menu(self):        
        while True:
            print("\t\t---- Admin Panel - Select an Option ----")
            print("\t\t\t1.View All Theatres")
            print("\t\t\t2.Select a Theatre")
            print("\t\t\t3.Add a Theatre")
            print("\t\t\t4.Exit")
            
            choice = input("👉 Enter your choice: ")

            if choice == "1":
                self.view_theatres()

            elif choice == "2":
                theatre_id = self.select_theatre()
                if theatre_id:
                    self.theatre_operations(theatre_id)

            elif choice == "3":
                self.add_theatre()

            elif choice == "4":
                print("\n👋 Exiting Admin Panel...")
                self.close_connection()
                break
            
            else:
                print("⚠️ Invalid choice. Please try again.")

    def get_next_theatre_id(self,cursor):
        """Fetch the next theatre ID in the format 'T01', 'T02'..."""
        cursor.execute("SELECT MAX(Theatre_ID) FROM theatre")
        last_id = cursor.fetchone()[0]
        if last_id:
            next_id = f"T{int(last_id[1:]) + 1:02d}"
        else:
            next_id = "T01"
        return next_id

    def add_theatre(self):
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="dbfm1"
        )
        cursor = connection.cursor()
        try:
            theatre_id = self.get_next_theatre_id(cursor)
            theatre_name = input("Enter Theatre Name: ")
            num_screens = int(input("Enter Number of Screens: "))

            cursor.execute("INSERT INTO theatre (Theatre_ID, Name_of_Theatre, No_of_Screens) VALUES (%s, %s, %s)",
                        (theatre_id, theatre_name, num_screens))

            for i in range(1, num_screens + 1):
                screen_id = f"{theatre_id}{i}"  # E.g., T011, T012, T021...
                no_row_gold = int(input(f"Enter Gold Rows for Screen {screen_id}: "))
                no_col_gold = int(input(f"Enter Gold Columns for Screen {screen_id}: "))
                no_row_silver = int(input(f"Enter Silver Rows for Screen {screen_id}: "))
                no_col_silver = int(input(f"Enter Silver Columns for Screen {screen_id}: "))

                availability_gold = "1" * (no_row_gold * no_col_gold)
                availability_silver = "1" * (no_row_silver * no_col_silver)

                cursor.execute("""INSERT INTO screen 
                    (Screen_ID, Theatre_ID, No_Row_Gold, No_Col_Gold, Availability_Gold, 
                    No_Row_Silver, No_Col_Silver, Availability_Silver) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                            (screen_id, theatre_id, no_row_gold, no_col_gold, availability_gold,
                                no_row_silver, no_col_silver, availability_silver))

            connection.commit()
            print(f"✅ Theatre '{theatre_name}' added successfully with {num_screens} screens.")

        except Exception as e:
            connection.rollback()
            print(f"❌ Error: {e}")

        finally:
            cursor.close()
            connection.close()
    def theatre_operations(self, theatre_id):
        """Operations that admin can perform for a selected theatre."""
        print(f"\n🎭 Managing Theatre: {theatre_id}")

        while True:
            print("\t\t----Theatre Management Options----")
            print("\t\t\t1.View Bookings")
            print("\t\t\t2.View Screens")
            print("\t\t\t3.View Shows")
            print("\t\t\t4.View Movies")
            print("\t\t\t5.Go Back to Main Menu")

            choice = input("👉 Enter your choice: ")

            if choice == "1":
                ManageBooking(theatre_id)
            elif choice == "2":
                ManageScreen(theatre_id)
            elif choice == "3":
                ManageShow(theatre_id)
            elif choice == "4":
                ManageMovie()
            elif choice == "5":
                print("\n🔙 Returning to Main Menu...")
                break
            else:
                print("⚠️ Invalid choice. Please try again.")