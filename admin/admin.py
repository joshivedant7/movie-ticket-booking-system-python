from .admin_base import AdminBase
from .mange_booking import ManageBooking
from .manage_screen import ManageScreen
from .manage_show import ManageShow
from .manage_movie import ManageMovie

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
            print("\t\t\t3.Exit")
            
            choice = input("👉 Enter your choice: ")

            if choice == "1":
                self.view_theatres()

            elif choice == "2":
                theatre_id = self.select_theatre()
                if theatre_id:
                    self.theatre_operations(theatre_id)  

            elif choice == "3":
                print("\n👋 Exiting Admin Panel...")
                self.close_connection()
                break
            
            else:
                print("⚠️ Invalid choice. Please try again.")

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