from .admin_base import AdminBase
import mysql.connector as sql

class ManageMovie(AdminBase):

    def __init__(self):
        super().__init__()
        self.movie_menu()

    def movie_menu(self):
        while True:
            print("\n🎬 Movie Management Menu:")
            print("1. Add Movie")
            print("2. Remove Movie")
            print("3. Update Movie")
            print("4. View Movies")
            print("5. Exit")
            choice = input("\nEnter choice: ")

            if choice == '1':
                self.add_movie()
            elif choice == '2':
                self.remove_movie()
            elif choice == '3':
                self.update_movie()
            elif choice == '4':
                self.view_movies()
            elif choice == '5':
                break
            else:
                print("⚠️ Invalid choice, please try again.")

    def add_movie(self):
        try:
            print("\n📝 Add New Movie")
            movie_id = input("Enter Movie ID: ")
            name = input("Enter Movie Name: ")
            language = input("Enter Language: ")
            genre = input("Enter Genre: ")

            target_audience_dict = {
                'U': 'Universal',
                'U/A': 'Parental Guidance',
                'A': 'Adult',
                'PG': 'Parental Guidance',
                'R': 'Restricted',
                'NC-17': 'No One Under 17 Admitted'
            }

            print("\nTarget Audience Options:")
            for key, value in target_audience_dict.items():
                print(f"{key}: {value}")

            target_audience = input("\nEnter Target Audience (U, U/A, A, PG, R, NC-17): ")

            if target_audience not in target_audience_dict:
                print("⚠️ Invalid Target Audience.")
                return

            query = """
                INSERT INTO movie (Movie_ID, Name, Language, Genre, Target_Audience)
                VALUES (%s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (movie_id, name, language, genre, target_audience))
            self.connection.commit()
            print("\n✅ Movie added successfully.")

        except sql.Error as e:
            print("❌ Error adding movie:", e)

    def remove_movie(self):
        try:
            movie_id = input("\nEnter Movie ID to remove: ")

            query = "DELETE FROM movie WHERE Movie_ID = %s"
            self.cursor.execute(query, (movie_id,))
            self.connection.commit()

            print("\n✅ Movie removed successfully.")
        except sql.Error as e:
            print("❌ Error removing movie:", e)

    def update_movie(self):
        try:
            movie_id = input("\nEnter Movie ID to update: ")

            print("Leave blank if no change.")
            new_name = input("Enter New Movie Name: ")
            new_language = input("Enter New Language: ")
            new_genre = input("Enter New Genre: ")

            target_audience_dict = {
                'U': 'Universal',
                'U/A': 'Parental Guidance',
                'A': 'Adult',
                'PG': 'Parental Guidance',
                'R': 'Restricted',
                'NC-17': 'No One Under 17 Admitted'
            }

            print("\nTarget Audience Options:")
            for key, value in target_audience_dict.items():
                print(f"{key}: {value}")

            new_target_audience = input("\nEnter New Target Audience (U, U/A, A, PG, R, NC-17): ")

            if new_target_audience and new_target_audience not in target_audience_dict:
                print("⚠️ Invalid Target Audience.")
                return

            update_query = "UPDATE movie SET "
            update_values = []

            if new_name:
                update_query += "Name = %s, "
                update_values.append(new_name)

            if new_language:
                update_query += "Language = %s, "
                update_values.append(new_language)

            if new_genre:
                update_query += "Genre = %s, "
                update_values.append(new_genre)

            if new_target_audience:
                update_query += "Target_Audience = %s, "
                update_values.append(new_target_audience)

            update_query = update_query.rstrip(", ")
            update_query += " WHERE Movie_ID = %s"
            update_values.append(movie_id)

            self.cursor.execute(update_query, tuple(update_values))
            self.connection.commit()

            print("\n✅ Movie updated successfully.")

        except sql.Error as e:
            print("❌ Error updating movie:", e)

    def view_movies(self):
        try:
            query = """
                SELECT Movie_ID, Name, Language, Genre, Target_Audience
                FROM movie
            """
            self.cursor.execute(query)
            movies = self.cursor.fetchall()

            if not movies:
                print("🚫 No movies found.")
                return

            print("\n🎬 Movies List:")
            print("-" * 80)
            print(f"{'Movie ID':<12}{'Name':<29}{'Language':<15}{'Genre':<17}{'Target Audience':<20}")
            print("-" * 80)

            for movie in movies:
                print(f"{movie[0]:<12}{movie[1]:<29}{movie[2]:<15}{movie[3]:<17}{movie[4]:<20}")
            
            print("-" * 80)

        except sql.Error as e:
            print("❌ Error fetching movies:", e)