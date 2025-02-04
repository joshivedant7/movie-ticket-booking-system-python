from .admin_base import AdminBase
import mysql.connector as sql

class ManageBooking(AdminBase):
    
    def __init__(self, theatre_id):
        super().__init__()
        self.theatre_id = theatre_id
        self.booking_menu()

    def booking_menu(self):
        while True:
            print("\n\t\t---- Booking Panel - Theatre: ", self.theatre_id, " ----")
            print("\t\t\t1. View All Bookings")
            print("\t\t\t2. Update Booking")
            print("\t\t\t3. Exit")
            
            choice = input("👉 Enter your choice: ")

            if choice == "1":
                self.view_bookings()

            elif choice == "2":
                self.update_booking()  

            elif choice == "3":
                print("\n👋 Exiting Booking Panel...")
                break
            
            else:
                print("⚠️ Invalid choice. Please try again.")

    def view_bookings(self):
        try:
            query = """
                SELECT B.Booking_ID, U.First_Name, U.Last_Name, S.Show_Date, S.Show_Time, 
                       B.No_of_Tickets, B.Total_Cost 
                FROM Booking B
                JOIN Web_user U ON B.User_ID = U.Web_User_ID
                JOIN Show_table S ON B.Show_ID = S.Show_ID
                JOIN Screen SC ON S.Screen_ID = SC.Screen_ID
                JOIN Theatre T ON SC.Theatre_ID = T.Theatre_ID
                WHERE T.Theatre_ID = %s
                ORDER BY S.Show_Date, S.Show_Time
            """
            self.cursor.execute(query, (self.theatre_id,))
            bookings = self.cursor.fetchall()

            if not bookings:
                print("\n🚫 No bookings found for this theatre.")
                return

            print("\n📜 Bookings List:")
            print("-" * 80)
            print(f"{'Booking ID':<12}{'User':<20}{'Show Date':<12}{'Show Time':<10}{'Tickets':<8}{'Total Cost':<10}")
            print("-" * 80)
            i=0
            for booking in bookings:
                print(f"{i}{booking[0]:<12}{booking[1]} {booking[2]:<18}{booking[3]:<12}{str(booking[4]):<10}{str(booking[5]):<8}{str(booking[6]):<10}")
                i+=1
            
            print("-" * 80)
        
        except sql.Error as e:
            print("❌ Error fetching bookings:", e)

    def update_booking(self):
        try:
            print("\n📝 Update Booking Details:")
            print("Leave blank if no change.")

            new_no_of_tickets = input("Enter New Number of Tickets (Leave blank to keep current): ")
            new_total_cost = input("Enter New Total Cost (Leave blank to keep current): ")
            new_card_number = input("Enter New Card Number (Leave blank to keep current): ")
            new_name_on_card = input("Enter New Name on Card (Leave blank to keep current): ")

            update_query = "UPDATE Booking SET "
            update_values = []
            
            if new_no_of_tickets:
                update_query += "No_of_Tickets = %s, "
                update_values.append(int(new_no_of_tickets))

            if new_total_cost:
                update_query += "Total_Cost = %s, "
                update_values.append(int(new_total_cost))
            
            if new_card_number:
                update_query += "Card_Number = %s, "
                update_values.append(new_card_number)
            
            if new_name_on_card:
                update_query += "Name_on_card = %s, "
                update_values.append(new_name_on_card)
            
            update_query = update_query.rstrip(", ")

            update_query += " WHERE Booking_ID = %s"

            booking_id = input('👉 Enter booking ID:')
            update_values.append(booking_id)

            self.cursor.execute(update_query, tuple(update_values))
            self.connection.commit()

            print("\n✅ Booking updated successfully.")

        except sql.Error as e:
            print("❌ Error updating booking:", e)