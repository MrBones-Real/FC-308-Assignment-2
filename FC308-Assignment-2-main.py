#FC308 Assignment 2

import csv

#intializing headers that are going to be used when writing into users.csv
headers = ["index", "username", "password", "mathLV", "mathHScore",
           "scienceLV","scienceHScore", "historyLV", "historyHScore",
           "artLV","artHScore", "computingLV", "computingHScore"]

#(W3Schools, 2026)
#(Python Documentation, 2026)
def main():
    userList = getUserList()
    
    while True:
        hasAccount = input("Do you already have an account? type yes(y) or no(n): ").strip().lower()
        if (hasAccount == 'yes' or hasAccount == 'y'):
            currentUser = logIn(userList)
            break
        
        elif (hasAccount == 'no' or hasAccount == 'n'):
            userList, currentUser = signUp(userList)
            break
            
        else:
            print("\nThat is not a valid input!\n")

    print(f"Welcome {currentUser['username']}!")

#Function that is going to get userList from users.csv or create the file if it doesn't exist
#(Python Documentation, 2026)
def getUserList():
    userList = []
    #Trying to open and getting data from users.csv
    try:
        with open("users.csv", 'r', newline = '') as file:
            reader = csv.DictReader(file)
            for row in reader:
                userList.append(row)
    #Creating the file if it doesn't exist
    except FileNotFoundError:
        with open("users.csv", 'w', newline = '') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()

    return userList

#This function will update the users.csv file with the new contact list
def updateUserList(users):
    with open("users.csv", 'w', newline = '') as file:
        writer = csv.DictWriter(file, fieldnames= headers)
        writer.writeheader()
        writer.writerows(users)

#This function checks if a username is already present in the user list
def isExistingUser(users, name):
    for user in users:
        if name == user["username"]:
            return True
    else:
        return False

#This function returns a user based on a username given
def getUser(users, name):
    for user in users:
        if name == user["username"]:
            return user
    
#This function will allow the user to create a new account
def signUp(users):
    print("\nSign-Up\n")
    #getting a user name that doesn't already exist
    while True:
        username = input("username: ")

        if isExistingUser(users, username):
            print("\nThat user already exists!\n")
        else:
            break
    #getting a password and getting the user to confirm it
    while True:
        password = input("password: ")
        confirmPassword = input("confirm password: ")

        if not password == confirmPassword:
            print("\nThe password does not coincide\n")
        else:
            break
    #creating the new user and adding it to the list
    newUser = {"index":len(users),"username":username, "password":password,
               "mathLV":'1', "mathHScore":'0', "scienceLV":'1', "scienceHScore":'0',
               "historyLV":'1', "historyHScore":'0', "artLV":'1', "artHScore":'0',
               "computingLV":'1', "computingHScore":'0'}
    
    users.append(newUser)
    updateUserList(users)
    print("Account created succesfully!")
    return users, newUser

#This function will allow user to log in into their account
def logIn(users):
    print("\nLog-In\n")
    #getting a username and making sure it exists in userlist
    while True:
        username = input("username: ")
        if isExistingUser(users, username):
            currentUser = getUser(users, username)
            break
        else:
            print("\nThat user doesn't exist!\n")
    #Asking the user for their password
    while True:
        password = input("password: ")

        if password == currentUser["password"]:
            print("\nLog In Successfull! :)\n")
            return currentUser
        else:
            print("\nWrong password :(\n")
            
main()
