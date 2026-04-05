#FC308 Assignment 2
#importing required libraries
import csv
import random

#intializing headers that are going to be used when writing into users.csv
headers = ["index", "username", "password", "mathLV", "mathHScore",
           "scienceLV","scienceHScore", "historyLV", "historyHScore",
           "artLV","artHScore", "computingLV", "computingHScore"]

#(W3Schools, 2026)
#(Python Documentation, 2026)
def main():
    #intializing main menu options
    mainMenu = ["Vocabulary builder","Play Game",
                "Check Stats","Check Ranking","Reset Progress","Exit"]
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
        selection = input("What do you want to do?: ").lower().strip()
        
        if selection == '1' or selection == "play game":
            playGame(currentUser)
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
    #initializing menus for the function
    subjectMenu = ["What subject do you want to practice?","Math","Science","History","Art","Computer Science"]
    levelMenu = ["What level do you want to play?","1","2","3"]
    gameSelectMenu = ["What game do you want to play?", "Word Guess", "Word Match"]
    #Allowing the user to select their subject
    while True:
        print()
        printMenu(subjectMenu)
        selection = input("Type number or name: ").lower().strip()

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
        print()
        printMenu(levelMenu)
        selection = input("Type number or name: ").lower().strip()

        if selection == '1':
            level = '1'
            break
        elif selection == '2':
            level = '2'
            break
        elif selection == '3':
            level = '3'
            break
        else:
            print("\nThat is not a valid input! >:(\n")

    #Allowing the user to choose a game
    while True:
        print()
        printMenu(gameSelectMenu)

        selection = input("Type number or name: ").lower().strip()

        if selection == '1' or selection == 'word guess':
            scoreAchieved = playWordGuess(subject, level)
            break
        elif selection == '2' or selection == 'Word Match':
            scoreAchieved = playWordMatch(subject, level)
            break
    

    print("\nGame Over!")
    print(f"Your score was: {scoreAchieved}")
#This function plays the word guess game for the user
#(W3 Schools, 2026)
def playWordGuess(subject, level):
    #Initializing menu for the game
    wordGuessMenu =["What do you want to do?", "Hint", "Guess"]
    #Getting a random word from the list and making sure it's from the subject and level selected
    wordList = getWordList()
    while True:
        wordToGuess = random.choice(wordList)
        if wordToGuess["subject"] == subject and wordToGuess["level"] == level:
            break
    #Game execution
    hintPenalty = 0
    mistakes = 0
    score = 0
    isGameOver = False
    displayedWord = []
    for i in range(len(wordToGuess["word"])):
        displayedWord.append("_ ")
    while not isGameOver:
        print("\nWord Guess!")
        print(f"Mistakes left: {4-mistakes}\n")
        print("".join(displayedWord))
        print()
        printMenu(wordGuessMenu)
        selection = input("Type number or option: ").lower().strip()
        #Asking the user if they want a hint or they want to guess
        if selection == "1" or selection == "hint":
            print(f"\nHint: {wordToGuess['definition']}\n")
            hintPenalty += 100
        elif selection == "2" or selection == "guess":
            #Asking the user for a letter and checking if it's on the selected word
            while True:
                guess = input("\nGuess a letter: ").lower().strip()
                if not len(guess) == 1 or not guess.isalpha():
                    print("\nThat is not a single letter!\n")
                else:
                    found = False
                    for i in range(len(wordToGuess["word"])):
                        if guess == wordToGuess["word"][i].lower():
                            found = True
                            displayedWord[i] = wordToGuess["word"][i] + " "
                    break
            if found:
                print("\nCorrect!\n")
            else:
                mistakes += 1
                print("\nIncorrect! Try again\n")
        else:
            print("\nThat is not a valid input!\n")
    #ending the game
        if mistakes == 4:
            print("\nToo bad!")
            isGameOver = True
        elif not "_ " in displayedWord:
            print("\nCongratulations!")
            isGameOver = True
            
    print(f"The word was: {wordToGuess['word']}\n")
    score = score + 1000 - (250 * mistakes) - hintPenalty

    return score

#(W3 Schools, 2026)
def playWordMatch(subject, level):
    #getting random words and building a list of definitions
    wordList = getWordList()
    filteredWordList = []
    definitionsToDisplay = []
    #Getting a random word to match
    for word in wordList:
        if word['subject'] == subject and word['level'] == level:
            filteredWordList.append(word)
    wordToMatch = random.choice(filteredWordList)
    definitionsToDisplay.append(wordToMatch["definition"].capitalize())
    #Building a list of random definitions
    for i in range(4):
        while True:
            randomWord = random.choice(filteredWordList)
            if not randomWord["definition"] in definitionsToDisplay:
                definitionsToDisplay.append(randomWord["definition"].capitalize())
                break
    random.shuffle(definitionsToDisplay)
    definitionsToDisplay.insert(0, "Definitions:\n")
    #Game execution
    isGameOver = False
    mistakes = 0
    while not isGameOver:
        print(f"\nMatch this Word!: {wordToMatch['word']}")
        print(f"Mistakes left: {4-mistakes}")
        printMenu(definitionsToDisplay)
        #Making sure the user's input is a valid input
        while True:
            guess = input("\nChoose: ").strip()
            if guess.isdigit() and len(guess) == 1 and int(guess) in range(1,6):
                break
            else:
                print("\nThat is not a valid input!\n")
        #Checking the users guess
        if definitionsToDisplay[int(guess)] == wordToMatch["definition"].capitalize():
            print("\nCongratulations That's correct!\n")
            isGameOver = True
        else:
            print("\nThat's Incorrect!\n")
            mistakes += 1
            if mistakes == 4:
                print("\nToo Bad!\n")
                isGameOver = True
            else:
                print("Try Again!\n")
    #Ending the game
    score = 1000 - (250 * mistakes)
    return score

main()
