import mysql.connector as sql

class AdminBase:

    def __init__(self):
        try:
            self.connection = sql.connect(
                host='localhost',
                user='root',
                password='',
                database='moviedb'
            )
            self.cursor = self.connection.cursor()
            print("✅ Database Connection Successful")
            return True
        except sql.Error as e:
            print("❌ Failed to connect to database:", e)
            return False

    def view_theatres(self):
        try:
            query = "SELECT * FROM Theatre"
            self.cursor.execute(query)
            theatres = self.cursor.fetchall()
            
            print("\n🎭 Available Theatres:")
            for theatre in theatres:
                print(f"ID: {theatre[0]}, Name: {theatre[1]}, Screens: {theatre[2]}, Area: {theatre[3]}")
        except sql.Error as e:
            print("❌ Error fetching theatres:", e)

    def select_theatre(self):
        theatre_id = input("\n🔹 Enter Theatre ID to manage: ")
        return theatre_id

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
    print("🔴 Database Connection Closed.")