import mysql.connector
from addFunctions import addObj, addColle, addExhibit
from editFunctions import editObj, editExhibit, editColle

def employeeMenu(connection):
    while True:
        print("\n************************************************************************************************************************\n")
        print("Welcome to the Employee Menu:")
        print("1.) Add Information")
        print("2.) Remove Information")
        print("3.) Edit Information")

        print("\n0.) Exit\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            addInfo(connection)
        elif choice == '2':
            removeInfo(connection)
        elif choice == '3':
            editInfo(connection)
        elif choice == '0':
            print("Exiting employee menu.")
            print("\n************************************************************************************************************************\n")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def addInfo(connection):
    while True:
        print("\n************************************************************************************************************************\n")
        print("Add Information Menu (You may go straight to adding objects, but will be prompted to add more information if nonexistent):\n")
        print("1.) Add Art Object")
        print("2.) Add Collection")
        print("3.) Add Exhibit")

        print("\n0.) Go Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            addObj(connection)
        elif choice == '2':
            addColle(connection)
        elif choice == '3':
            addExhibit(connection)
        elif choice == '0':
            print("Returning to Employee Menu.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


    

def removeInfo(connection):
    try:
        cursor = connection.cursor()
        display_query = "SELECT obj_ID, title FROM art_object"
        cursor.execute(display_query)
        artworks = cursor.fetchall()

        print("\nArt Objects:")
        for artwork in artworks:
            print(f"Artwork ID: {artwork[0]}, {artwork[1]}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        print("Failed to display Art Objects.")
        return

    print("\nRemoving Art Object:")
    object_id = input("Enter Art Object ID to remove: ")
    try:
        cursor = connection.cursor()

        check_artist_query = f"SELECT artist_name FROM artist WHERE obj_ID = {object_id}"
        cursor.execute(check_artist_query)
        artists = cursor.fetchall()

        if artists:
            print(f"Associated artist found. Deleting associated artist(s) first...")

            for artist in artists:
                artist_name = artist[0]
                deleteQuery = f"DELETE FROM artist WHERE artist_name = '{artist_name}'"
                cursor.execute(deleteQuery)
                connection.commit()

                if cursor.rowcount > 0:
                    print(f"Artist {artist_name} deleted successfully.")
                else:
                    print(f"Failed to delete artist {artist_name}.")

        deleteQuery = f"DELETE FROM art_object WHERE obj_ID = {object_id}"
        cursor.execute(deleteQuery)
        connection.commit()

        if cursor.rowcount > 0:
            print("Art Object removed successfully.")
        else:
            print(f"No Art Object found with ID {object_id}.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        print("Failed to remove Art Object, returning to Main Menu.")



def editInfo(connection):
    while 1:
        print("\n************************************************************************************************************************\n")
        print("Welcome to the EDIT menu.")
        print("NOTE: You cannot edit object ID or artist name.")
        print("Instead you must remove the object and then re add the information through ADD menu.\n")
        print("1.) Edit Object Information")
        print("2.) Edit Existing Collections")
        print("3.) Edit Existing Exhibitions\n")

        print("0.) Exit\n")

        editchoice = input("Enter your choice: ")

        if editchoice == "1":
            print("\n************************************************************************************************************************\n")
            editObj(connection)

        elif editchoice == '2':
            print("\n************************************************************************************************************************\n")
            editColle(connection)

        elif editchoice =='3':
            print("\n************************************************************************************************************************\n")
            editExhibit(connection)
        elif editchoice == '0':
            print("Exiting Edit Menu.")
            break
        else:
            print("Invalid Option.")
    
