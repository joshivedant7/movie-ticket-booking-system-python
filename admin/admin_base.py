import mysql.connector as sql

class AdminBase:

    def __init__(self):
        try:
            self.connection = sql.connect(
                host='localhost',
                user='admin',
                password='admin',
                database='dbfm1'
            )
            self.cursor = self.connection.cursor()
            print("✅ Database Connection Successful")
            return True
        except sql.Error as e:
            print("❌ Failed to connect to database:", e)
            return False

    def view_theatres(self):
        try:
            query = "SELECT * FROM theatre;"
            self.cursor.execute(query)
            theatres = self.cursor.fetchall()
            
            print("\n🎭 Available Theatres:")
            for theatre in theatres:
                print(f"ID: {theatre[0]}, Name: {theatre[1]}, Screens: {theatre[2]}, Area: {theatre[3]}")
        except sql.Error as e:
            print("❌ Error fetching theatres:", e)

    def select_theatre(self):
        theatre_id = input("\n🔹 Enter Theatre ID to manage: ").upper()
        query = "SELECT Theatre_ID FROM theatre;"
        self.cursor.execute(query)
        theatres = self.cursor.fetchall()
        theatre_ids = [row[0] for row in theatres]
        if theatre_id in theatre_ids :
            return theatre_id
        else : raise Exception(f'No theater-id with {theatre_id}')

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
    # print("🔴 Database Connection Closed.")