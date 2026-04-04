#FC308 Assignment 2

import csv

#intializing headers that are going to be used when writing into users.csv
headers = ["index", "username", "password", "mathLV", "mathHScore",
           "scienceLV","scienceHScore", "historyLV", "historyHScore",
           "artLV","artHScore", "computingLV", "computingHScore"]
#intializing main menu options
mainMenu = ["Vocabulary builder","Play Game",
            "Check Stats","Check Ranking","Reset Progress","Exit"]
#initializing subject selection menu
subjectMenu = ["What subject do you want to practice?","Math","Science","History","Art","Computer Science"]
#initializing level selection menu
levelMenu = ["What level do you want to play?","1","2","3"]

#(W3Schools, 2026)
#(Python Documentation, 2026)
def main():
    #getting the user list
    userList = getUserList()
    #handling log-in or sign-up
    while True:
        hasAccount = input("Do you already have an account? type yes(y) or no(n): ").strip().lower()
        if (hasAccount == 'yes' or hasAccount == 'y'):
            currentUser = logIn(userList)
            break
        elif (hasAccount == 'no' or hasAccount == 'n'):
            userList, currentUser = signUp(userList)
            break    
        else:
            print("\nThat is not a valid input!")       
    #main menu
    while True:
        print(f"\nWelcome {currentUser['username']}!")
        printMenu(mainMenu)
        print()
        selection = input("What do you want to do?: ")
        selection = selection.lower().strip()
        print(selection)
        
        if selection == '1' or selection == "play game":
            playGame()
        elif selection == '2' or selection == "check stats":
            print("\nChecking Stats!\n")
        elif selection == '3' or selection == "check ranking":
            print("\nChecking Ranking!\n")
        elif selection == '4' or selection == "reset progress":
            print("\nResetting Progress\n")
        elif selection == '5' or selection == "exit":
            print("\nThank you for playing! :)\n")
            break
        else:
            print("\nThat is not a valid input!\n")

#Function that is going to get the wordList for the games
#(code academy, 2026)
def getWordList():
    wordList = []
    #Trying to open and getting data from words.csv
    try:
        with open("words.csv", 'r', newline = '') as file:
            reader = csv.DictReader(file)
            for row in reader:
                wordList.append(row)
            return wordList
    #Warning the user that they don't have the file
    except FileNotFoundError:
        print("\nWARNING")
        print("'words.csv' is not within the local files")
        print("Please make sure that 'words.csv' is located in the same folder this python document is")
        exit()
                
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

#This function prints a menu
def printMenu(menu):
    i = 0
    for item in menu:
        if (i == 0):
            print(item)
        else:
            print(f"{i}) {item}")
            
        i += 1
    print()

#This function will allow the user to choose a subject, level and game to play
def playGame(user):
    #Allowing the user to select their subject
    while True:
        printMenu(subjectMenu)

        selection = input("Type number or name: ")
        selection = selection.lower().stripped()

        if selection == '1' or selection == "math":
            subject = 'math'
            break
        elif selection == '2' or selection == "science":
            subject = 'science'
            break
        elif selection == '3' or selection == "history":
            subject = 'history'
            break
        elif selection == '4' or selection == "art":
            subject = 'art'
            break
        elif selection == '5' or selection == "computer science":
            subject = 'computer science'
            break
        else:
            print("\nThat is not a valid input! >:(\n")
    #Allowing the user to choose their level
    while True:
        printMenu(levelMenu)

        selection = input("Type number or name: ")
        selection = selection.lower().stripped()

        if selection == '1':
            level = '1'
            break
        elif selection == '2':
            level = '2'
            break
        elif selection == '3':
            level = '3'
            break
        else.
            print("\nThat is not a valid input! >:(\n")

    playWordGuess(subject, level)
#This function plays the word guess game for the user
def playWordGuess(subject, level):
    wordList = getWordList()
    filteredWordList = []
    
    for word in wordList:
        if word[subject] == subject and word[level] == level:
            filteredWordList.append(word)

    print(filteredWordList)
    
main()
