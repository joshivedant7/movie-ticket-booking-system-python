from .admin_base import AdminBase
import mysql.connector as sql

class ManageShow(AdminBase):
    def __init__(self, theatre_id):
        super().__init__()
        self.theatre_id = theatre_id
        self.screen_ids = self.get_screen_ids()  
        self.show_menu()

    def get_screen_ids(self):
        """Fetch available screen IDs for the selected theatre."""
        try:
            query = "SELECT Screen_ID FROM Screen WHERE Theatre_ID = %s"
            self.cursor.execute(query, (self.theatre_id,))
            screen_ids = [screen[0] for screen in self.cursor.fetchall()]
            if not screen_ids:
                print("🚫 No screens found for this theatre.")
            return screen_ids
        except sql.Error as e:
            print("❌ Error fetching screen IDs:", e)
            return []

    def show_menu(self):
        while True:
            print("\n\t\t---- Show Management - Theatre ID:", self.theatre_id, "----")
            print("\t\t\t1.View Shows")
            print("\t\t\t2.Add Show")
            print("\t\t\t3.Update Show")
            print("\t\t\t4.Remove Show")
            print("\t\t\t5.Go Back to Theatre Menu")

            choice = input("👉 Enter your choice: ")

            if choice == "1":
                self.view_shows()
            elif choice == "2":
                self.add_show()
            elif choice == "3":
                self.update_show()
            elif choice == "4":
                self.remove_show()
            elif choice == "5":
                print("\n🔙 Returning to Theatre Menu...")
                break
            else:
                print("⚠️ Invalid choice. Please try again.")

    def view_shows(self):
        try:
            if not self.screen_ids:
                print("🚫 No screens available for this theatre.")
                return

            placeholders = ', '.join(['%s'] * len(self.screen_ids))
            query = f"""
                SELECT Show_ID, Show_Time, Show_Date, Seats_Remaining_Gold, Seats_Remaining_Silver,
                    Class_Cost_Gold, Class_Cost_Silver, Movie_ID
                FROM show_table
                WHERE Screen_ID IN ({placeholders})
                ORDER BY Show_Date, Show_Time
            """

            self.cursor.execute(query, tuple(self.screen_ids))
            shows = self.cursor.fetchall()

            if not shows:
                print("🚫 No shows found for the selected screens in this theatre.")
                return

            print("\n🎬 Shows List for Theatre ID:", self.theatre_id)
            print("-" * 80)
            print(f"{'Show ID':<12}{'Time':<10}{'Date':<12}{'Gold Seats':<12}{'Silver Seats':<12}{'Gold Cost':<10}{'Silver Cost':<12}{'Movie ID':<10}")
            print("-" * 80)

            for show in shows:
                print(f"{show[0]:<12}{show[1]}{show[2]}{show[3]:<12}{show[4]:<12}{show[5]:<10}{show[6]:<12}{show[7]}")

            print("-" * 80)
        except sql.Error as e:
            print("❌ Error fetching shows:", e)

    def add_show(self):
        try:
            print("\n📝 Add New Show")

            show_id = input("Enter Show ID: ")
            show_time = input("Enter Show Time (HH:MM:SS): ")
            show_date = input("Enter Show Date (YYYY-MM-DD): ")
            seats_gold = int(input("Enter Gold Seats Remaining: "))
            seats_silver = int(input("Enter Silver Seats Remaining: "))
            cost_gold = int(input("Enter Gold Class Cost: "))
            cost_silver = int(input("Enter Silver Class Cost: "))

            if not self.screen_ids:
                print("🚫 No screens available for this theatre.")
                return

            print("\nAvailable Screen IDs:", self.screen_ids)
            screen_id = input("Enter Screen ID from the above list: ")

            if screen_id not in self.screen_ids:
                print("⚠️ Invalid Screen ID.")
                return

            movie_id = input("Enter Movie ID: ")

            query = """
                INSERT INTO show_table (Show_ID, Show_Time, Show_Date, Seats_Remaining_Gold, Seats_Remaining_Silver,
                                        Class_Cost_Gold, Class_Cost_Silver, Screen_ID, Movie_ID)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (show_id, show_time, show_date, seats_gold, seats_silver,
                                        cost_gold, cost_silver, screen_id, movie_id))
            self.connection.commit()
            print("\n✅ Show added successfully.")
            
        except sql.Error as e:
            print("❌ Error adding show:", e)

    def update_show(self):
        try:
            show_id = input("\nEnter Show ID to update: ")

            print("Leave blank if no change.")
            new_show_time = input("Enter New Show Time (HH:MM:SS): ")
            new_show_date = input("Enter New Show Date (YYYY-MM-DD): ")
            new_seats_gold = input("Enter New Gold Seats Remaining: ")
            new_seats_silver = input("Enter New Silver Seats Remaining: ")
            new_cost_gold = input("Enter New Gold Class Cost: ")
            new_cost_silver = input("Enter New Silver Class Cost: ")
            
            if not self.screen_ids:
                print("🚫 No screens available for this theatre.")
                return
            
            print("\nAvailable Screen IDs:", self.screen_ids)
            new_screen_id = input("Enter New Screen ID: ")

            if new_screen_id not in self.screen_ids:
                print("⚠️ Invalid Screen ID.")
                return

            new_movie_id = input("Enter New Movie ID: ")

            update_query = "UPDATE show_table SET "
            update_values = []

            if new_show_time:
                update_query += "Show_Time = %s, "
                update_values.append(new_show_time)

            if new_show_date:
                update_query += "Show_Date = %s, "
                update_values.append(new_show_date)

            if new_seats_gold:
                update_query += "Seats_Remaining_Gold = %s, "
                update_values.append(int(new_seats_gold))

            if new_seats_silver:
                update_query += "Seats_Remaining_Silver = %s, "
                update_values.append(int(new_seats_silver))

            if new_cost_gold:
                update_query += "Class_Cost_Gold = %s, "
                update_values.append(int(new_cost_gold))

            if new_cost_silver:
                update_query += "Class_Cost_Silver = %s, "
                update_values.append(int(new_cost_silver))

            if new_screen_id:
                update_query += "Screen_ID = %s, "
                update_values.append(new_screen_id)

            if new_movie_id:
                update_query += "Movie_ID = %s, "
                update_values.append(new_movie_id)

            update_query = update_query.rstrip(", ")
            update_query += " WHERE Show_ID = %s"
            update_values.append(show_id)

            self.cursor.execute(update_query, tuple(update_values))
            self.connection.commit()
            print("\n✅ Show updated successfully.")

        except sql.Error as e:
            print("❌ Error updating show:", e)

    def remove_show(self):
        try:
            show_id = input("\nEnter Show ID to remove: ")
            query = "DELETE FROM Show WHERE Show_ID = %s"
            self.cursor.execute(query, (show_id,))
            self.connection.commit()
            print("\n✅ Show removed successfully.")
        except sql.Error as e:
            print("❌ Error removing show:", e)