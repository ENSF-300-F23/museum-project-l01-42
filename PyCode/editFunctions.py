import mysql.connector

def editExhibit(connectMe):
    try:
        cursor = connectMe.cursor()

        display_query = "SELECT exhibit_ID, Ename FROM EXHIBITION"
        cursor.execute(display_query)
        exhibitions = cursor.fetchall()

        print("\nExhibitions:")
        for exhibition in exhibitions:
            print(f"Exhibition ID: {exhibition[0]}, {exhibition[1]}")

        print("\nEditing Exhibition:")
        exhibit_id = input("Enter Exhibition ID to edit: ")

        check_exhibit_query = "SELECT * FROM EXHIBITION WHERE exhibit_ID = %s"
        cursor.execute(check_exhibit_query, (exhibit_id,))
        existing_exhibit = cursor.fetchone()

        if existing_exhibit:
            print("\n************************************************************************************************************************\n")
            print("\nCurrent Details:")
            print(f"Exhibition Name: {existing_exhibit[1]}")
            print(f"Start Date: {existing_exhibit[2]}")
            print(f"End Date: {existing_exhibit[3]}")

            new_name = input("\nEnter new exhibition name (or press Enter to keep the current name): ")
            new_start_date = input("Enter new start date (or press Enter to keep the current start date): ")
            new_end_date = input("Enter new end date (or press Enter to keep the current end date): ")

            update_query = """
                UPDATE EXHIBITION
                SET Ename = %s, start_date = %s, end_date = %s
                WHERE exhibit_ID = %s
            """
            cursor.execute(update_query, (new_name or existing_exhibit[1], new_start_date or existing_exhibit[2], new_end_date or existing_exhibit[3], exhibit_id))
            connectMe.commit()

            print("Exhibition details updated successfully.")
        else:
            print(f"No Exhibition found with ID {exhibit_id}.\nIf you are trying to create a new Exhibition ID, please use the Add Exhibition Function instead.")

    except mysql.connector.Error as err:
        connectMe.rollback()
        print(f"Error: {err}")
        print("Failed to edit Exhibition details.")

def editColle(connectMe):
    try:
        cursor = connectMe.cursor()

        while True:
            try:
                display_query = "SELECT * FROM COLLECTIONS"
                cursor.execute(display_query)
                collections = cursor.fetchall()

                print("\nCollections:")
                for collection in collections:
                    print(collection)

            except mysql.connector.Error as err:
                print(f"Error: {err}")
                print("Failed to display Collections.")

            print("\nEditing Collection:")
            collection_name = input("Enter the name of the collection to edit (or 'exit' to return): ")

            if collection_name.lower() == 'exit':
                break

            check_collection_query = "SELECT * FROM COLLECTIONS WHERE collection_name = %s"
            cursor.execute(check_collection_query, (collection_name,))
            existing_collection = cursor.fetchone()

            if existing_collection:
                print("\nCurrent Collection Details:")
                for i, column in enumerate(cursor.description):
                    print(f"{column[0]}: {existing_collection[i]}")

                update_values = {}
                for i, column in enumerate(cursor.description):
                    new_value = input(f"Enter new {column[0]} (or press Enter to keep the current value): ")
                    update_values[column[0]] = new_value or existing_collection[i]

                update_query = f"""
                    UPDATE COLLECTIONS
                    SET {', '.join([f'{key} = %s' for key in update_values.keys()])}
                    WHERE collection_name = %s
                """
                cursor.execute(update_query, tuple(update_values.values()) + (collection_name,))
                connectMe.commit()

                print("Collection details updated successfully.")
            else:
                print(f"No collection found with name {collection_name}.\nIf you are trying to create a new collection, please use Add Collection function.")

    except mysql.connector.Error as err:
        connectMe.rollback()
        print(f"Error: {err}")
        print("Failed to edit Collection details.")


def editObj(connectMe):
    try:
        cursor = connectMe.cursor()

        while True:
            try:
                display_query = "SELECT * FROM ART_OBJECT"
                cursor.execute(display_query)
                objects = cursor.fetchall()

                print("\nArt Objects:")
                for obj in objects:
                    obj_id, title, *_ = obj
                    print(f"ID: {obj_id}, Title: {title}")
                    print("----------------------")

            except mysql.connector.Error as err:
                print(f"Error: {err}")
                print("Failed to display Art Objects.")

            print("\nEditing Art Object:")
            obj_id = input("Enter the ID of the art object to edit (0 to return): ")

            if obj_id.lower() == '0':
                break

            check_obj_query = "SELECT * FROM ART_OBJECT WHERE obj_ID = %s"
            cursor.execute(check_obj_query, (obj_id,))
            existing_obj = cursor.fetchone()

            print("\n************************************************************************************************************************\n")

            if existing_obj:
                print("Current Art Object Details:")
                print(f"ID: {existing_obj[0]}")
                print(f"Title: {existing_obj[1]}")
                print(f"Description: {existing_obj[2]}")
                print(f"Year Created: {existing_obj[3]}")
                print(f"Origin: {existing_obj[4]}")
                print(f"Epoch: {existing_obj[5]}")
                print(f"Collection: {existing_obj[6]}")
                print(f"Artist: {existing_obj[7]}")
                print(f"Exhibit ID: {existing_obj[8]}\n")

                update_values = {}

                #DEBUG issue here

                for i, column in enumerate(cursor.description):
                    if column[0] not in ['obj_ID', 'artist_name']:
                        new_value = input(f"Enter new {column[0]} (or press Enter to keep the current value): ")

                        if column[0] in ['collection_name', 'exhibit_ID']:
                            table_name = 'collections' if column[0] == 'collection_name' else 'exhibition'
                            if new_value != '' and not doesExist(connectMe, column[0], new_value, table_name):
                                print(f"{column[0]} '{new_value}' does not exist. Please enter a valid {column[0]}.")
                                break

                        update_values[column[0]] = new_value or existing_obj[i]

                #DEBUG issue here

                if len(update_values) == len(cursor.description) - 2:  
                    update_query = f"""
                        UPDATE ART_OBJECT
                        SET {', '.join([f'{key} = %s' for key in update_values.keys()])}
                        WHERE obj_ID = %s
                    """
                    cursor.execute(update_query, tuple(update_values.values()) + (obj_id,))
                    connectMe.commit()

                    print("Art Object details updated successfully.")
            else:
                print(f"No art object found with ID {obj_id}.\n If you are trying to create a new ID, please use ADD functions instead.")

    except mysql.connector.Error as err:
        connectMe.rollback()
        print(f"Error: {err}")
        print("Failed to edit Art Object details.")


def doesExist(connectMe, column_name, value, table_name):
    try:
        cursor = connectMe.cursor()
        check_query = f"SELECT * FROM {table_name} WHERE {column_name} = %s"
        cursor.execute(check_query, (value,))
        result = cursor.fetchone()
        return result is not None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False


