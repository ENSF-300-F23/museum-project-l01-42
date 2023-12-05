import mysql.connector

def adminMenu(connection):
    while True:
        print("\n************************************************************************************************************************\n")
        print("Welcome to the ADMIN Menu:\n")
        print("1.) Add a new user")
        print("2.) Edit a user")
        print("3.) Block a user")
        print("4.) Make changes to the database")

        print("\n0.) Exit\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            addNewUser()
        elif choice == '2':
            editUser()
        elif choice == '3':
            blockUser()
        elif choice == '4':
            makeDatabaseChanges()
        elif choice == '0':
            print("Exiting admin menu.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def addNewUser():
    # Implement logic to add a new user
    print("Adding a new user. Under construction.")

def editUser():
    # Implement logic to edit a user
    print("Editing a user. Under construction.")

def blockUser():
    # Implement logic to block a user
    print("Blocking a user. Under construction.")

def makeDatabaseChanges():
    while True:
        print("\n************************************************************************************************************************\n")
        print("Database Changes Menu:")
        print("1. Add a new table")
        print("2. Modify table attributes")
        print("3. Add constraints to a table")
        print("0. Exit")

        dbChoice = input("Enter your choice: ")

        if dbChoice == '1':
            addNewTable()
        elif dbChoice == '2':
            modifyTableAttributes()
        elif dbChoice == '3':
            addConstraints()
        elif dbChoice == '0':
            print("Exiting database changes menu.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def addNewTable():
    # Implement logic to add a new table
    print("Adding a new table. Under construction.")

def modifyTableAttributes():
    # Implement logic to modify table attributes
    print("Modifying table attributes. Under construction.")

def addConstraints():
    # Implement logic to add constraints to a table
    print("Adding constraints to a table. Under construction.")
