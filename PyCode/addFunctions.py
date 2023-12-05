import mysql.connector

def addObj(connectMe):
    try:
        cursor = connectMe.cursor()

        obj_ID = input("Enter the obj_ID for the art object (XXXXX): ")
        title = input("Enter the title of the art object: ")
        descript = input("Enter a description of the art object: ")
        year_created = input("Enter the year the art object was created: ")
        origin = input("Enter the country origin of the art object: ")
        epoch = input("Enter the epoch of the art object: ")

        collection_name = input("Enter the name of the collection: ")
        check_collection_query = "SELECT collection_name FROM COLLECTIONS WHERE collection_name = %s"
        cursor.execute(check_collection_query, (collection_name,))
        existing_collection = cursor.fetchone()

        if not existing_collection:
            print(f"Collection '{collection_name}' does not exist. Do you want to create a new one?")
            create_new_collection = input("Enter 'y' for yes, 'n' for no: ")
            if create_new_collection.lower() == 'y':
                addColle(connectMe)
            else:
                print("Aborted. Collection not added.")
                return

        artistExist = input("Does the art object have an associated artist? (y/n): ")

        if artistExist.lower() == 'y':
            artistName = input("Enter the name of the artist: ")
            descript = input("Enter a description of the artist: ")
            dateBorn = input("Enter the date the artist was born (YYYY-MM-DD): ")
            didDie = input("Enter the date the artist died (If inapplicable type NULL, otherwise in YYYY-MM-DD): ")
            if didDie.upper() == 'NULL':
                didDie = None

            
            artistOrigin = input("Enter the country of origin of the artist: ")
            style = input("Enter the artistic style of the artist: ")
            epoch = input("Enter the artistic epoch of the artist: ")

            insert_artist_query = """
                INSERT INTO ARTIST (artist_name, descript, date_born, date_died, country_of_orgin, style, epoch, obj_ID)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_artist_query, (artistName, descript, dateBorn, didDie, artistOrigin, style, epoch, obj_ID))

        exhibit_ID = input("Enter the exhibit_ID for the art object (9XXXX): ")

        if exhibit_ID:
            check_exhibit_query = "SELECT exhibit_ID FROM EXHIBITION WHERE exhibit_ID = %s"
            cursor.execute(check_exhibit_query, (exhibit_ID,))
            existing_exhibit = cursor.fetchone()

            if not existing_exhibit:
                print(f"Exhibit '{exhibit_ID}' does not exist. Creating New Entry...")
                addExhibit(connectMe)

        insertQuery = """
            INSERT INTO ART_OBJECT (obj_ID, title, descript, year_created, origin, epoch, collection_name, exhibit_ID)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insertQuery, (obj_ID, title, descript, year_created, origin, epoch, collection_name, exhibit_ID))
        

        connectMe.commit()

        print("Art object added successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        print("Failed to add Art Object.")

def addExhibit(connectMe):
    try:
        cursor = connectMe.cursor()

        exhibit_ID = input("Enter the exhibit_ID for the exhibit (9XXXX): ")
        Ename = input("Enter the name of the exhibit: ")
        start_date = input("Enter the start date of the exhibit (YYYY-MM-DD): ")
        end_date = input("Enter the end date of the exhibit (YYYY-MM-DD): ")

        insertQuery = """
            INSERT INTO EXHIBITION (exhibit_ID, Ename, start_date, end_date)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(insertQuery, (exhibit_ID, Ename, start_date, end_date))
        connectMe.commit()

        print("Exhibit added successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        print("Failed to add Exhibit.")

def addColle(connectMe):
    try:
        cursor = connectMe.cursor()

        collection_name = input("Enter the name of the collection: ")

        while 1:
            Ctype = input("Enter the type of the collection -- P for Permanent | B for Borrowed: ")
            if Ctype.upper() == 'P':
                Ctype = "Permanent"
                break
            elif Ctype.upper() == 'B':
                Ctype = "Borrowed"
                break
            else:
                print("Invalid Choice - has to be (P/B)")

        descript = input("Enter a description of the collection: ")
        address = input("Enter the address of the collection: ")
        phone = input("Enter the phone number of the collection: ")
        current_contact = input("Enter the current contact person of the collection: ")

        insert_collection_query = """
            INSERT INTO COLLECTIONS (collection_name, Ctype, descript, address, phone, current_contact)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_collection_query, (collection_name, Ctype, descript, address, phone, current_contact))

        if Ctype == 'Permanent':
            pstatus = input("Enter the status of the permanent collection (On Display, Stored, etc.): ")
            cost = int(input("Enter the cost of the permanent collection: "))
            date_acquired = input("Enter the date the permanent collection was acquired (YYYY-MM-DD): ")

            insert_permanent_query = """
                INSERT INTO PERMANENT_COLLECTION (collection_name, Pstatus, cost, date_acquired)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(insert_permanent_query, (collection_name, pstatus, cost, date_acquired))
        elif Ctype == 'Borrowed':
            date_returned = input("Enter the date the collection was returned (or press Enter for none, YYYY-MM-DD): ")
            date_borrowed = input("Enter the date the collection was borrowed (YYYY-MM-DD): ")

            insert_borrowed_query = """
                INSERT INTO BORROWED_COLLECTION (borrowed_from, date_returned, date_borrowed)
                VALUES (%s, %s, %s)
            """
            cursor.execute(insert_borrowed_query, (collection_name, date_returned, date_borrowed))

        connectMe.commit()

        print("Collection added successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        print("Failed to add Collection.")

