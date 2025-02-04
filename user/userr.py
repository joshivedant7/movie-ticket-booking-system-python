from rich.align import Align
from rich.box import ROUNDED
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.console import Console
from .db_setup import get_cursor
from termcolor import colored
from user import User 

x = False

def getMovies():
    """Fetch movie_id and movie_name from the movies table."""
    query = "SELECT Movie_ID, Name ,Language , Genre , Target_Audience FROM movie"

    # Get both connection and cursor
    connection, cursor = get_cursor()

    if cursor:
        try:
            # Execute the query using the cursor
            cursor.execute(query)

            # Fetch all rows from the query result
            rows = cursor.fetchall()
            if len(rows) == 0:
                print("data not found")

                return True

            # Print the fetched rows (movie_id and movie_name)
            for row in rows:
                print("Movie ID : ", row[0])
                print("Movie    :", row[1])
                print("Language :", row[2])
                print("Genre    :", row[3])
                print("Audience :", row[4])
                print(
                    "_____________________________________________________________________________________________________________")

            # Close the cursor and the connection after use
            cursor.close()
            connection.close()
        except Exception as e:
            print(f"Error executing query: {e}")
    else:
        print("Failed to get cursor, check DB connection!")


def getTheatres():
    query = "SELECT Theatre_ID, Name_of_Theatre, Area FROM theatre"

    connection, cursor = get_cursor()

    if cursor:
        try:
            cursor.execute(query)

            rows = cursor.fetchall()
            if len(rows) == 0:
                print("data not found")

                return True

            for row in rows:
                theatre_id, theatre_name, area = row
                print(
                    f"Theatre ID: {theatre_id},  Name: {theatre_name} , Area : {area}")
            cursor.close()
            connection.close()
        except Exception as e:
            print(f"Error executing query: {e}")
    else:
        print("Failed to get cursor, check DB connection!")
    print()


def getScreenId(mid, Theatre_ID):
    query = """
    SELECT Screen_ID, Show_ID, Show_Time, Show_Date, 
           Seats_Remaining_Gold, Seats_Remaining_Silver, 
           Class_Cost_Gold, Class_Cost_Silver 
    FROM show_table 
    WHERE Movie_Id = %s AND Screen_ID LIKE %s
    """

    connection, cursor = get_cursor()

    if cursor:
        try:
            like_pattern = f"{Theatre_ID}%"

            cursor.execute(query, (mid, like_pattern))

            rows = cursor.fetchall()
            if len(rows) == 0:
                print("data not foundxx")
                return True
            for row in rows:
                # print(f"Screen ID: {row[0]}, Show ID: {row[1]}, Show Time: {row[2]}, Show Date: {row[3]}")
                # print(f"Seats Remaining (Gold): {row[4]}, Seats Remaining (Silver): {row[5]}")
                # print(f"Class Cost (Gold): {row[6]}, Class Cost (Silver): {row[7]}")
                print("Show id : ", row[1])
                print("Screen id : ", row[0])
                print("show-Date : ", row[3])
                print("show-time : ", row[2])
                print("Remaining Gold seats : ", row[4])
                print("Remaining Silver seats : ", row[5])

                print("-" * 100)
                print()
                print("        Gold seat Cost : ",
                      row[6], "            Silver seat Cost : ", row[7])
                print()
                print("-"*100)
                print()

            cursor.close()
            connection.close()
        except Exception as e:
            print(f"Error executing query: {e}")
    else:
        print("Failed to get cursor, check DB connection!")


def getSilverSeats(screen_id, theatre_id):
    query = "SELECT  Availability_Silver FROM screen where Screen_ID = %s AND Theatre_ID = %s "

    connection, cursor = get_cursor()

    if cursor:
        try:
            cursor.execute(query, (screen_id, theatre_id))

            rows = cursor.fetchall()
            if len(rows) == 0:
                print("data not found")
                return True
            for row in rows:

                return row[0]

            cursor.close()
            connection.close()
        except Exception as e:
            print(f"Error executing query: {e}")
    else:
        print("Failed to get cursor, check DB connection!")


def getGoldSeats(screen_id, theatre_id):
    query = "SELECT  Availability_Gold FROM screen where Screen_ID = %s AND Theatre_ID = %s "

    connection, cursor = get_cursor()

    if cursor:
        try:
            cursor.execute(query, (screen_id, theatre_id))

            rows = cursor.fetchall()
            if len(rows) == 0:
                print("data not found")
                return True
            for row in rows:

                return row[0]

            cursor.close()
            connection.close()
        except Exception as e:
            print(f"Error executing query: {e}")
    else:
        print("Failed to get cursor, check DB connection!")


def get_row_col(screen_id):
    query = "SELECT No_Row_Gold, No_Col_Gold, No_Row_Silver, No_Col_Silver FROM screen WHERE Screen_ID = %s"

    connection, cursor = get_cursor()

    if cursor:
        try:
            cursor.execute(query, (screen_id,))  
            rows = cursor.fetchall()
            if len(rows) == 0:
                print("data not found")
                return True
            if not rows:
                print(f"No data found for Screen_ID: {screen_id}")
                return None

            return [rows[0][0], rows[0][1], rows[0][2], rows[0][3]]
        except Exception as e:
            print(f"Error executing query: {e}")
        finally:
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()
    else:
        print("Failed to get cursor, check DB connection!")
        return None


def display_theatre(gold_seats, silver_seats, screen_id):
    gold_seats = gold_seats.replace(" ", "")
    silver_seats = silver_seats.replace(" ", "")

    list2 = get_row_col(screen_id)
    if list2 is None:
        print("Failed to fetch row and column data.")
        return

    gr, gc, sr, sc = list2
    console = Console()

    title = Align.center(
        Panel.fit(
            Text("CINEPLEX THEATRE", style="bold white"),
            box=ROUNDED,
            border_style="gold3",
            padding=(1, 10)
        )
    )
    console.print(title)

    gold_table = Table(
        title="GOLD CLASS PREMIUM",
        box=ROUNDED,
        show_header=False,
        title_style="bold gold3",
        title_justify="center",
    )

    for _ in range(gc):
        gold_table.add_column(justify="center", min_width=8)

    seat_num = 1
    for i in range(gr):
        row = []
        for j in range(gc):
            is_available = gold_seats[i * gc + j] == '1'
            seat_text = Text(f"{seat_num:03d}", style="bold black")
            row.append(Panel(
                seat_text,
                box=ROUNDED,
                style="green" if is_available else "red",
                padding=(0, 2)  
            ))
            seat_num += 1
        gold_table.add_row(*row)

    console.print(Align.center(gold_table))
    console.print()

    silver_table = Table(
        title="SILVER CLASS",
        box=ROUNDED,
        show_header=False,
        title_style="bold grey70",
        title_justify="center",
    )

    for _ in range(sc):
        silver_table.add_column(justify="center", min_width=8)

    for i in range(sr):
        row = []
        for j in range(sc):
            if seat_num > len(silver_seats) + len(gold_seats):
                break
            is_available = silver_seats[i * sc + j] == '1'
            seat_text = Text(f"{seat_num:03d}", style="bold black")
            row.append(Panel(
                seat_text,
                box=ROUNDED,
                style="green" if is_available else "red",
                padding=(0, 2)
            ))
            seat_num += 1
        silver_table.add_row(*row)

    console.print(Align.center(silver_table))
    console.print()

    screen = Align.center(
        Panel(
            Text("SCREEN THIS WAY", style="bold white"),
            box=ROUNDED,
            border_style="blue",
            padding=(1, 4)
        )
    )
    console.print(screen)

    legend = Table.grid(padding=2)
    legend.add_row(
        Panel(" ", style="green", box=ROUNDED),
        Text("Available", style="white"),
        Panel(" ", style="red", box=ROUNDED),
        Text("Booked", style="white")
    )
    console.print(Align.center(legend))


def get_ticket_cost(show_id):

    query = "SELECT Class_Cost_Gold, Class_Cost_Silver , Seats_Remaining_Gold , Seats_Remaining_Silver FROM show_table WHERE Show_ID = %s"

    connection, cursor = get_cursor()

    if cursor:
        try:
            cursor.execute(query, (show_id,))

            rows = cursor.fetchall()
            if len(rows) == 0:
                print("data not found")
                return True
            if not rows:
                return None  # No data found

            return [rows[0][0], rows[0][1], rows[0][2], rows[0][3]]
        except Exception as e:
            print(f"Error executing query: {e}")
        finally:
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()
    else:
        print("Failed to get cursor, check DB connection!")
        
        return None
    
def bookSeat(strSilver_list, strGold_list, show_id):
    if True:
        bool = False
        nseats = int(input("Enter number of seats you want to book: "))
        if nseats > 10:
            print("no more than 10 seats at a time ")
            return True
        total_amt = 0
        gold_seats = ['1']*len(strGold_list)
        silver_seats = ['1']*len(strSilver_list)
        total_seats = 0
        list3 = get_ticket_cost(show_id)
        silvercost = list3[1]
        goldcost = list3[0]

        gold = 0
        silver = 0

        # Iterate over the number of seats to be booked
        for i in range(nseats):
            print(f"Enter {i+1}th seat number: ")
            sn = int(input())

            if sn >= 1 and sn <= len(strGold_list) and strGold_list[sn - 1] == "1":
                # Change the corresponding seat to '0' (booked) in the Gold seats list
                strGold_list[sn - 1] = '0'
                total_amt += goldcost
                gold_seats[sn-1] = '0'
                total_seats += 1
                gold += 1
                bool = True
            elif sn <= len(strSilver_list)+len(strGold_list) and sn > len(strGold_list) and strSilver_list[sn - len(strGold_list) - 1] == "1":
                # Change the corresponding seat to '0' (booked) in the Silver seats list
                strSilver_list[sn - len(strGold_list) - 1] = '0'
                total_amt += silvercost
                silver_seats[sn-len(strGold_list)-1] = '0'
                total_seats += 1
                silver += 1
                bool = True

            else:
                print("Seat not available")

        # Convert the updated lists back to strings
        strGold = ''.join(strGold_list)
        strSilver = ''.join(strSilver_list)
        gold_seats1 = ''.join(gold_seats)
        silver_seats1 = ''.join(silver_seats)

        # Print the updated seat availability
        print()
        
        return [total_amt, strGold, strSilver, gold_seats1, silver_seats1, total_seats, bool,list3[2]-gold , list3[3]-silver]

def updateseats(x,y,show_id):
    query = """
    UPDATE show_table 
    SET Seats_Remaining_Gold = %s,Seats_Remaining_Silver = %s
    WHERE  Show_ID = %s 
    """
    connection, cursor = get_cursor()

    if cursor:
        try:
            # Execute the update query using the cursor
            cursor.execute(query, (x, y, show_id))

            # Commit the changes to the database
            connection.commit()

        except Exception as e:
            print(f"Error updating seat availability: {e}")
        finally:
            # Close the cursor and the connection
            cursor.close()
            connection.close()
    else:
        print("Failed to get cursor, check DB connection!")

def updateSeatAvailability(strGold, strSilver, theatre_id, screen_id):
    # Define the query to update the availability of Gold and Silver seats
    tid = theatre_id
    query = """
    UPDATE screen 
    SET Availability_Gold = %s, Availability_Silver = %s
    WHERE  Screen_ID = %s 
    """

    # Get the database connection and cursor
    connection, cursor = get_cursor()

    if cursor:
        try:
            # Execute the update query using the cursor
            cursor.execute(query, (strGold, strSilver, screen_id))

            # Commit the changes to the database
            connection.commit()

        except Exception as e:
            print(f"Error updating seat availability: {e}")
        finally:
            # Close the cursor and the connection
            cursor.close()
            connection.close()
    else:
        print("Failed to get cursor, check DB connection!")

def generate_booking_id():
    try:
        connection, cursor = get_cursor()

        # Query to find the maximum booking_id in the table
        query = "SELECT MAX(booking_id) FROM booking"
        cursor.execute(query)
        result = cursor.fetchone()[0]

        if result:
            # Extract the numeric portion of the booking_id and increment it
            # Skip the first two characters ("BK")
            numeric_part = int(result[2:])
            new_numeric_part = numeric_part + 1
        else:
            # Default starting value if the table is empty
            new_numeric_part = 10000001

        # Format the new booking_id
        new_booking_id = f"BK{new_numeric_part:08d}"  # Zero-padded to 8 digits
        return new_booking_id

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None


def insert_booking_record(total_seats, total_cost, fname, lname, uid, show_id, gold_seats, silver_seats, strGold, strSilver, screen_id, bool,gold , silver):
    try:
        bk_id = generate_booking_id()  # Make sure this function returns a valid ID
        if bool == False:
            print("no seat to book")
            return

        print("----------------------------------------------------")
        print("   Total amount to be paid : ", total_cost)
        print("----------------------------------------------------")
        print()

        card_no = input(
            "Enter your 15-digit card number to pay  / 0 to Exit : ")

        if card_no == "1":
            return
        elif len(card_no) != 15:
            print("Enter valid 15 digit card number ")
            return
        updateseats(gold, silver, show_id)
        
        print()
        print("seat confirmed!")
        print()
        updateSeatAvailability(strGold, strSilver, "-1", screen_id)
        print()

        name = fname + " " + lname
        # Ensure this returns a valid connection and cursor
        connection, cursor = get_cursor()

        if cursor:
            query = """
            INSERT INTO `booking`
            (`Booking_ID`, `No_of_Tickets`, `Total_Cost`, `Card_Number`, `Name_on_card`, `User_ID`, `Show_ID`, `Gold_Seats`, `Silver_Seats`) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            # Ensure the values match the column order
            try:
                cursor.execute(query, (bk_id, total_seats, total_cost,
                               card_no, name, uid, show_id, gold_seats, silver_seats))
                connection.commit()

            except Exception as e:
                print(f"Error executing query: {e}")
                connection.rollback()  # Rollback the transaction in case of error
            finally:
                cursor.close()
                connection.close()
        else:
            print("Failed to get cursor, check DB connection!")
    except Exception as e:
        print(f"Error: {e}")

def getMovieByShow_ID(show_id):
    movie_id = -1
    movie = ""
    try:
        connection, cursor = get_cursor()
        if cursor:
            query1 = "SELECT Movie_ID FROM show_table WHERE Show_ID = %s"  # Assuming Shows table
            cursor.execute(query1, (show_id,))
            rows = cursor.fetchall()
            if len(rows) == 0:
                print("data not found")
                return True

            if rows:  # Check if rows are not empty
                movie_id = rows[0][0]

                # Fetch movie name by Movie_ID
                query2 = "SELECT Name FROM movie WHERE Movie_ID = %s"  # Assuming Movies table
                cursor.execute(query2, (movie_id,))
                rows1 = cursor.fetchall()

                if rows1:  # Check if rows1 is not empty
                    movie = rows1[0][0]
                    return movie
                else:
                    print("Movie not found for Movie_ID:", movie_id)
            else:
                print("Show_ID not found:", show_id)

    except Exception as e:
        print(f"Error: {e}")
    return None

def get_sc_id(show_id):
    try:
        connection, cursor = get_cursor()
        if cursor:
            query1 = "SELECT Screen_ID FROM show_table WHERE Show_ID = %s"  # Assuming Show table
            cursor.execute(query1, (show_id,))  # Wrap show_id in a tuple
            rows = cursor.fetchall()
            if len(rows) == 0:
                print("data not found")
                return True

            if rows:  # Check if rows are not empty
                # print("__________________________________________________________________")
                print()
                return rows[0][0]
            else:
                print("No screen found for this Show_ID.")

    except Exception as e:
        print(f"Error: {e}")

def cancelTickets():
    g_seats = ""
    s_seats = ""
    real_g_seats = ""
    real_s_seats = ""
    show_id = ""
    try:
        connection, cursor = get_cursor()
        if cursor:
            query1 = "SELECT Booking_ID, Show_ID, No_of_Tickets FROM booking WHERE User_ID = %s"
            # Wrap user.u.User.User.web_uid in a tuple
            cursor.execute(query1, (u.web_uid,))
            rows = cursor.fetchall()
            if len(rows) == 0:
                print("data not found")
                return True

            if rows:
                print()
                for row in rows:
                    print("Booking ID:", row[0], end=" | ")
                    movie_name = getMovieByShow_ID(row[1])
                    if movie_name:
                        print("Movie:", movie_name, end=" | ")
                    print("No. of seats booked:", row[2])
                    print()
            else:
                print("No bookings found for this user.")
    except Exception as e:
        print(f"Error: {e}")

    b_id = input("Enter a Booking ID / 0 to Exit : ")
    if b_id == "0":
        return
    sc_id = ""
    try:
        connection, cursor = get_cursor()
        if cursor:
            query1 = "SELECT Show_ID, Gold_Seats, Silver_Seats FROM booking WHERE Booking_ID = %s"
            cursor.execute(query1, (b_id,))  # Wrap b_id in a tuple
            rows = cursor.fetchall()
            if len(rows) == 0:
                print("data not found")
                return True
            if rows:
                print()
                sc_id = get_sc_id(rows[0][0])
                show_id = rows[0][0]
                g_seats = rows[0][1]
                s_seats = rows[0][2]
            else:
                print("No bookings found for this Booking ID.")
    except Exception as e:
        print(f"Error: {e}")
    
    try:
        connection, cursor = get_cursor()
        if cursor:
            query1 = "SELECT Availability_Gold, Availability_Silver FROM screen WHERE Screen_ID = %s"
            cursor.execute(query1, (sc_id,))  # Wrap sc_id in a tuple
            rows = cursor.fetchall()
            if len(rows) == 0:
                print("data not found")
                return True
            if rows:
                print()
                # Convert string to list for mutability
                real_g_seats = list(rows[0][0])
                # Convert string to list for mutability
                real_s_seats = list(rows[0][1])
            else:
                print("No screen found for this Screen_ID.")
    except Exception as e:
        print(f"Error: {e}")
        
        
        
    gold = 0
    silver  = 0
    

    # Modify the seats
    try:
        for i in range(len(real_g_seats)):
            if g_seats[i] == '0':  # Compare characters
                gold+=1
                real_g_seats[i] = '1'  # Update the seat

        for i in range(len(real_s_seats)):
            if s_seats[i] == '0':  # Compare characters
                silver+=1
                real_s_seats[i] = '1'  # Update the seat
                
                
        # gold , silver , show_id , 

        # Convert lists back to strings
        real_g_seats = "".join(real_g_seats)
        real_s_seats = "".join(real_s_seats)

        updateSeatAvailability(real_g_seats, real_s_seats, "-1", sc_id)
    except Exception as e:
        print(f"Error while modifying seats: {e}")
    
    list4 = get_ticket_cost(show_id)
    updateseats(list4[2]+gold , list4[3]+silver , show_id)
    try:
        connection, cursor = get_cursor()
        if cursor:
            query1 = "DELETE FROM `booking` WHERE Booking_ID = %s"
            cursor.execute(query1, (b_id,))  # Wrap b_id in a tuple
            connection.commit()  # Commit changes to the database
            print("Booking successfully canceled.")
    except Exception as e:
        print(f"Error: {e}")

def view_booking():
    try:
        connection, cursor = get_cursor()
        if cursor:
            query1 = "SELECT Booking_ID, Show_ID, No_of_Tickets ,Total_Cost FROM booking WHERE User_ID = %s"
            # Wrap user.u.User.User.web_uid in a tuple
            cursor.execute(query1, (u.web_uid,))
            rows = cursor.fetchall()
            if len(rows) == 0:
                print("data not found")
                return True
            if rows:
                print(
                    "___________________________________________________________________________________________________________")
                for row in rows:
                    print("Booking ID:", row[0], end=" | ")
                    movie_name = getMovieByShow_ID(row[1])
                    if movie_name:
                        print("Movie:", movie_name, end=" | ")
                    print("No. of seats booked:", row[2], end=" | ")
                    print("Total Cost : ", row[3])
            else:
                print("No bookings found for this user.")
    except Exception as e:
        print(f"Error: {e}")

def staring_point(user):   
    u = user 
    while True:
        print()
        print("1. book tickets")
        print("2. cancellation of tickets")
        print("3. view all your bookings")
        print("0. exit ")
        print()
        n = input("enter a choice[0-2] : ")

        if n == "0":
            break

        elif n == "1":
            print()
            getMovies()

            print()
            movie_id = input("enter a movie id : ")
            print()
            getTheatres()
            theatre_id = input("enter a theatre id : ")

            print()
            x1 = getScreenId(movie_id, theatre_id)
            if x1:
                continue

            print()
            show_id = input("enter a show id : ")

            query = """
                SELECT Screen_ID, Class_Cost_Gold, Class_Cost_Silver
                FROM show_table
                WHERE Show_ID = %s
                """
            connection, cursor = get_cursor()
            cursor.execute(query, (show_id,))
            rows = cursor.fetchall()
            screen_id = "1"
            class_cost_gold = "1"
            class_cost_silver = "1"
            if len(rows) == 0:
                print("data not found")
                print()
                continue
            if rows:
                # screen_id, class_cost_gold, class_cost_silver = row
                # print(f"Screen ID: {screen_id}")
                # print(f"Class Cst (Gold): {class_cost_gold}")
                # print(f"Class Cost (Silver): {class_cost_silver}")
                list4 = rows
                screen_id = list4[0][0]
                class_cost_gold = list4[0][1]
                class_cost_silver = list4[0][1]
            else:
                print("No data found for the given Show_ID.")
            cursor.close()
            connection.close()
            print()
            print(screen_id, class_cost_gold, class_cost_silver)

        # Get the seat availability strings
            strSilver = getSilverSeats(screen_id, theatre_id)

            strGold = getGoldSeats(screen_id, theatre_id)

            if x == True:
                x = False
                continue

            # Remove spaces from the strings
            strSilver = strSilver.replace(" ", "")
            strGold = strGold.replace(" ", "")

            # Convert the strings to lists for mutability
            strSilver_list = list(strSilver)
            strGold_list = list(strGold)

            display_theatre(strGold, strSilver, screen_id)
            if x == True:
                x = False
                continue

            list1 = bookSeat(strSilver_list, strGold_list, show_id)
            if x == True:
                x = False
                continue
            if (list1 == True):
                continue
            if list1[6] == True:
                insert_booking_record(list1[5], list1[0], u.fname,u.lname, u.web_uid,
                                    show_id, list1[3], list1[4], list1[1], list1[2], screen_id, list1[6],list1[7] , list1[8])
            # total_seats , total_cost ,fname, lname ,uid , show_id ,silver_seats,gold_seats
            
        elif n == "2":
            x1 = cancelTickets()
            if x1:
                continue
        elif n == "3":
            x1 = view_booking()
            if x1:
                continue
        else:
            print("enter a valid choice")