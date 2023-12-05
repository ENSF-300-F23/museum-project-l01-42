import mysql.connector
from admin import adminMenu
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

def userLevel():
    while True:
        print("Who is using the program?:")
        usertype = input("Admin = (1) | Guest (0) \nYour Choice: ")
        if usertype == '1' or usertype == '0':
            if usertype == '1':
                adminMenu()
            elif usertype == '0':
                guestMenu()
            break
        else:
            print("Invalid choice, enter a user type.")

def main():
    introMenu()
    userLevel()

main()