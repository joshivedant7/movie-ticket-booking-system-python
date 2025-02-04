import mysql.connector

def create_connection():
    """Establish and return a connection to the database."""
    try:
        conn = mysql.connector.connect(
            host="localhost",        
            user="root",             
            password="",             
            database="moviedb"
        )
        
        if conn.is_connected():
            return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def get_cursor():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        return connection, cursor
    print("get_cursor: Failed to connect to the database.")
    return None, None
