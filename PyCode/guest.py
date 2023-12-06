import mysql.connector

def guestMenu(connection):
    while True:
        print("\n************************************************************************************************************************\n")
        print("Welcome to the GUEST Menu:\n")
        print("1.) View all Artworks")
        print("2.) View all Exhibitions")
        print("3.) View all Artists")
        print("4.) View all Collections\n")

        print("0.) Exit\n")

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
            print("\n************************************************************************************************************************\n")
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
                        paint_query = f"SELECT * FROM PAINTING WHERE obj_ID={objectID}"
                        cursor.execute(paint_query)
                        paint_art = cursor.fetchall()

                        sculp_query = f"SELECT * FROM SCULPTURE WHERE obj_ID={objectID}"
                        cursor.execute(sculp_query)
                        sculp_art = cursor.fetchall()

                        statue_query = f"SELECT * FROM STATUE WHERE obj_ID={objectID}"
                        cursor.execute(statue_query)
                        statue_art = cursor.fetchall()

                        other_query = f"SELECT * FROM OTHER WHERE obj_ID={objectID}"
                        cursor.execute(other_query)
                        other_art = cursor.fetchall()

                        print("\nAdditional Information:")
                        if paint_art:
                            print("\nType: Painting")
                        elif sculp_art:
                            print("\nType: Sculpture")
                        elif statue_art:
                            print("\nType: Statue")
                        elif other_art:
                            print("\nType: Other")

                        for artwork in details:
                            print()
                            print(f"Artwork ID: {artwork[0]}\nTitle: {artwork[1]}")
                            print(f"Description: {artwork[2]}\nYear: {artwork[3]}\nOrigin: {artwork[4]}")
                            print(f"Epoch: {artwork[5]}\nCollection: {artwork[6]}\nArtist: {artwork[7]}\nExhibit ID: {artwork[8]}")
                        if paint_art:
                            for data in paint_art:
                                print(f"Drawn Using: {data[1]}\nDrawn on: {data[2]}\nStyle: {data[3]}")
                                print()
                        elif sculp_art:
                            for data in sculp_art:
                                print(f"Material: {data[1]}\nHeight: {data[2]} Meters\nWeight: {data[3]} Kg\nStyle: {data[4]}")
                                print()
                        elif statue_art:
                            for data in statue_art:
                                print(f"Material: {data[1]}\nHeight: {data[2]} Meters\nWeight: {data[3]} Kg\nStyle: {data[4]}")
                                print()
                        elif other_art:
                            for data in other_art:
                                print(f"Art Type: {data[1]}\nStyle: {data[2]}")
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
            runQuery = "SELECT artist_name, Descript FROM artist"
            cursor.execute(runQuery)
            getMe = cursor.fetchall()
            print()
            for index in getMe:
                print(f"Artist Name: {index[0]}")
                print(f"Description: {index[1]}")
                print()
            
            while True:
                art_name = input("For further information on artists type the artist name. To continue on type 0: ")
                if art_name != '0':
                    detailsQuery = f"SELECT * FROM artist WHERE artist_name = '{art_name}'"
                    cursor.execute(detailsQuery)
                    details = cursor.fetchall()
                    if details:

                        print("\nAdditional Information:")
                        for name in details:
                            print()
                            print(f"Artist Name: {name[0]}\nObject ID: {name[1]}\nDescription: {name[2]}\nDate of Birth: {name[3]}")
                            print(f"Date of Death: {name[4]}\nOrigin: {name[5]}\nStyle: {name[6]}\nEpoch: {name[7]}")
                            print()
                    else:
                        print("No additional information found for the specified artist name.")
                elif art_name == '0':
                    break
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
            print()
            cursor = dbc.cursor()
            runQuery = "SELECT collection_name, descript FROM collections"
            cursor.execute(runQuery)
            getMe = cursor.fetchall()
            for index in getMe:
                print(f"Collection Name: {index[0]}")
                print(f"Description: {index[1]}")
                print()

            while True:
                collection_name = input("For further information on collections type the collection name. To continue on type 0: ")
                if collection_name != '0':
                    detailsQuery = f"SELECT * FROM collections WHERE collection_name = '{collection_name}'"
                    cursor.execute(detailsQuery)
                    details = cursor.fetchall()
                    if details:
                        permanent_query = f"SELECT * FROM PERMANENT_COLLECTION WHERE collection_name='{collection_name}'"
                        cursor.execute(permanent_query)
                        permanent_coll = cursor.fetchall()

                        borrowed_query = f"SELECT * FROM BORROWED_COLLECTION WHERE borrowed_from='{collection_name}'"
                        cursor.execute(borrowed_query)
                        borrowed_coll = cursor.fetchall()

                        print("\nAdditional Information:")
                        
                        if permanent_coll:
                            print("\nType: Permanent Collection")
                        elif borrowed_coll:
                            print("\nType: Borrowed Collection")

                        for collect in details:
                            print()
                            print(f"Collection Name: {collect[0]}\nType: {collect[1]}")
                            print(f"Description: {collect[2]}\nAddress: {collect[3]}\nPhone: {collect[4]}\nCurrent Contact: {collect[5]}")
                        
                        if permanent_coll:
                            for data in permanent_coll:
                                print(f"Status: {data[1]}\nCost: ${data[2]}\nDate Acquired: {data[3]}")
                                print()
                        elif borrowed_coll:
                            for data in borrowed_coll:
                                print(f"Date Borrowed: {data[2]}")
                                if data[1] == None:
                                    print("Date Returned: Still in Possession.")
                                print()
                    else:
                        print("No additional information found for the specified collection name.")
                elif collection_name == '0':
                    break
        else:
            print("Could not connect to the database.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        print("Failed to view exhibitions.")