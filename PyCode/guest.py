import mysql.connector

def guestMenu(connection):
    while True:
        print("\n************************************************************************************************************************\n")
        print("Welcome to the GUEST Menu:\n")
        print("1.) View all Artworks")
        print("2.) View all Exhibitions")
        print("3.) View all Artists")
        print("4.) View all Collections\n")

        print("\n0. Exit\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            viewArtworks(connection)
        elif choice == '2':
            viewExhibitions(connection)
        elif choice == '3':
            viewArtists(connection)
        elif choice == '4':
            viewColle(connection)
        elif choice == '0':
            print("Exiting guest menu.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def viewArtworks(dbc):
    try:
        if dbc and dbc.is_connected():
            print("\n************************************************************************************************************************\n")
            print("Viewing All Art Objects on Hand:")

            cursor = dbc.cursor()
            runQuery = "SELECT obj_ID, title FROM art_object"
            cursor.execute(runQuery)
            getMe = cursor.fetchall()
            print()
            for index in getMe:
                print(f"Artwork ID: {index[0]}")
                print(f"Title: {index[1]}")
                print()

            while True:
                objectID = input("For further information on objects type the ID. To continue on type 0: ")
                if objectID != '0':
                    detailsQuery = f"SELECT * FROM art_object WHERE obj_ID = {objectID}"
                    cursor.execute(detailsQuery)
                    details = cursor.fetchall()
                    if details:
                        print("\nAdditional Information:")
                        for artwork in details:
                            print()
                            print(f"Artwork ID: {artwork[0]}\nTitle: {artwork[1]}")
                            print(f"Description: {artwork[2]}\nYear: {artwork[3]}\nOrgin: {artwork[4]}")
                            print(f"Epoch: {artwork[5]}\nCollection: {artwork[6]}\nArtist: {artwork[7]}\nExhibit ID: {artwork[8]}")
                            print()
                    else:
                        print("No additional information found for the specified ID.")
                elif objectID == '0':
                    break
        else:
            print("Could not connect to the database.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        print("Unknown Error Occured, returning to main menu.")

def viewExhibitions(dbc):
    try:
        if dbc and dbc.is_connected():
            print("\n************************************************************************************************************************\n")
            print("Viewing Art Objects' Exhibitions:")

            cursor = dbc.cursor()
            runQuery = "SELECT * FROM exhibition"
            cursor.execute(runQuery)
            getMe = cursor.fetchall()

            for exhibit in getMe:
                print()
                print(f"Exhibit ID: {exhibit[0]}\nName: {exhibit[1]}\nStart Date: {exhibit[2]}\nEnd Date: {exhibit[3]}")
                print()
        else:
            print("Could not connect to the database.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        print("Failed to view exhibitions.")

def viewArtists(dbc):
    try:
        if dbc and dbc.is_connected():
            print("\n************************************************************************************************************************\n")
            print("Viewing Participating Artists:")

            cursor = dbc.cursor()
            runQuery = "SELECT * FROM artist"
            cursor.execute(runQuery)
            getMe = cursor.fetchall()

            for name in getMe:
                print()
                print(f"Artist Name: {name[0]}\nObject ID: {name[1]}\nDescription: {name[2]}\nDate of Birth: {name[3]}")
                print(f"Date of Death: {name[4]}\nOrgin: {name[5]}\nStyle: {name[6]}\nEpoch: {name[7]}")
                print()
        else:
            print("Could not connect to the database.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        print("Failed to view exhibitions.")

def viewColle(dbc):
    try:
        if dbc and dbc.is_connected():
            print("\n************************************************************************************************************************\n")
            print("Viewing Participating Collections:")

            cursor = dbc.cursor()
            runQuery = "SELECT * FROM collections"
            cursor.execute(runQuery)
            getMe = cursor.fetchall()

            for collect in getMe:
                print()
                print(f"Collection Name: {collect[0]}\nType: {collect[1]}\n")
                print(f"Description: {collect[2]}\nAddress: {collect[3]}\nPhone: {collect[4]}\nCurrent Contact: {collect[5]}")
                print()
        else:
            print("Could not connect to the database.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        print("Failed to view exhibitions.")