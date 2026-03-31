#FC308 Assignment 2

import csv

#(W3Schools, 2026)
def main():

    userList = getUserList()

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
    try:
        with open("users.csv", 'r', newline = '') as file:
            reader = csv.DictReader(file)
            for (row in reader):
                userList.append(row)
    except FileNotFoundError:
        with open("users.csv", 'w', newline = '') as file:
            fieldnames = ["username", "password", "mathLV", "mathHScore","scienceLV", "scienceHScore", "historyLV", "historyHScore", "artLV", "artHScore", "computingLV", "computingHScore"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

    return userList
