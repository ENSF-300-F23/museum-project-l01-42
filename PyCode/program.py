import mysql.connector
from employee import employeeMenu
from guest import guestMenu

def introMenu():
    while True:
        print("\n************************************************************************************************************************\n")
        print("Welcome to the Arts Museum Database Management System.")

        try:
            password = input('Enter database password (whatever is used to login to MySQL): ') 

            database_login = {
                'user': 'root',
                'password': password,
                'host': 'localhost',
                'database': 'museum'
            }
            
            connectme = mysql.connector.connect(**database_login)

            if connectme.is_connected():
                print("Connected.\n")
                break
            else:
                print("Could not connect. Please try again.\n")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            print("Could not connect. Please try again.\n")
    return connectme

def userLevel(database):
    while True:
        print("Who is using the program?:")
        usertype = input("(Guest = 0) | (Employee = 1) | (Close Program = EXIT)\nYour Choice: ")
        if usertype == '1' or usertype == '0':
            if usertype == '0':
                guestMenu(database)
            elif usertype == '1':
                employeeMenu(database)
        elif usertype.upper() == "EXIT":
            print("Closing Program.")
            break
        else:
            print("Invalid choice, enter a user type.")

    database.close()
    print("closed connection")

def main():
    db = introMenu()
    userLevel(db)
    

main()