import mysql.connector

def guestMenu():
    while True:
        print("\n************************************************************************************************************************\n")
        print("Welcome to the GUEST Menu:\n")
        print("1.) View all artworks")
        print("2.) View all exhibitions")
        print("3.) View all Artists\n")

        print("\n0. Exit\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            viewArtworks()
        elif choice == '2':
            viewExhibitions()
        elif choice == '3':
            viewArtists()
        elif choice == '0':
            print("Exiting guest menu.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def viewArtworks():
    print("\n************************************************************************************************************************\n")
    print("Viewing all artworks. Under construction.")

def viewExhibitions():
    print("\n************************************************************************************************************************\n")
    print("Viewing all exhibitions. Under construction.")

def viewArtists():
    print("\n************************************************************************************************************************\n")
    print("Viewing all Artists. Under construction.")

