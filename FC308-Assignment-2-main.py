#FC308 Assignment 2

import csv

#(W3Schools, 2026)
def main():

    userList = getUserList()
    print(userList)

    while True:
        hasAccount = input("Do you already have an account? type yes(y) or no(n): ").strip().lower()
        if (hasAccount == 'yes' or hasAccount == 'y'):
            #logIn()
            print("LogIn!")
        
        elif (hasAccount == 'no' or hasAccount == 'n'):
            #signUp()
            print("SignUp!")
        
        else:
            print("\nThat is not a valid input!\n")

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
            fieldnames = ["username", "password", "mathLV", "mathHScore","scienceLV",
                          "scienceHScore", "historyLV", "historyHScore", "artLV",
                          "artHScore", "computingLV", "computingHScore"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

    return userList

def signUp(users):
    while True:
        username = input("username: ")
        
        if username in users:
            print("\nThat user already exists!\n")
        else:
            break

    while True:
        password = input("password: ")
        confirmPassword = input("confirm password: ")

        if not password == confirmPassword:
            print("The password does not coincide")
        else:
            break

    newUser = ["username":username, "password":password, "mathLV":'1', "mathHScore":'0', "scienceLV":'1', "scienceHScore":'0', "historyLV":'1', "historyHScore":'0', "artLV":'1', "artHScore":'0', "computingLV":'1', "computingHighScore":'0']
    users.append(newUser)
    #updateUserList()
    return users

main()
