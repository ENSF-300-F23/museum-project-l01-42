import mysql.connector

#user type, 1 = admin, 0 = guest
usertype = '0'

while (1):
    print("\n************************************************************\n")
    print("Welcome to the Arts Museum Database Managment System.")
    print("Who is using the program?:")
    usertype = input("Admin = (1) | Guest (0) \nYour Choice: ")

    while (1):
        if usertype == '1':
            password = input('Enter admin password: ')

            if (password == 'Jeromebarcelona01!'):
                database_login = {
                    'user': 'root',
                    'password': password,
                    'host':'localhost',
                    'database': 'museum'
                }
                connectme = mysql.connector.connect(**database_login)
                if connectme.is_connected():
                    print("Connected.\n")
                    break
                else:
                    print("Could not connect.\n")
                    break
            else:
                print("Password Declined.")
                print("Re-enter a valid credential.\n")
        elif usertype == '0':
            database_login = {
                    'user': 'root',
                    'password':'Jeromebarcelona01!',
                    'host':'localhost',
                    'database': 'museum'
                }
            connectme = mysql.connector.connect(**database_login)
            if connectme.is_connected():
                print("Connected.\n")
                break
            else:
                print("Could not connect.\n")
                break


if usertype == '1':
    print("nice")

elif usertype == '0':
    print("guest")