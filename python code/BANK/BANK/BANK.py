import csv
import time
import sys

loggedIN = False
Account_Balance = 0
names = []
with open("bankList.csv", "r") as bankListRead:
    reader = csv.DictReader(bankListRead)
    for dicT in reader:
        names.append(dicT["Name"])


def Create_acccount():
    global names
    global Account_Balance
    with open("bankList.csv", "a", newline='') as bankList:
        Account_Balance = 0
        headers = ["Name", "Email", "Pin",
                   "Password", "Phone_Number", "Country", "Account_Balance"]
        writer = csv.DictWriter(bankList, fieldnames=headers)
        name = input("Name: ")
        if name in names:
            print("Account exists,Try again!!")
            Create_acccount()
        else:
            pass
        email = input("Email Adress: ")
        pin = input("Pin: ")
        password = input("Password: ")
        country = input("Country: ")
        phone_Number = input("Phone Number: ")
        writer.writerow({"Name": name, "Email": email, "Pin": pin,
                         "Password": password, "Phone_Number": phone_Number, "Country": country, "Account_Balance": Account_Balance})
        print("Please wait........")
        time.sleep(2.2)
        print("Account created succesfully,Login to check your balance.")


def login():
    global loggedIN
    with open("bankList.csv", "r") as bankListRead:
        readerLogin = csv.DictReader(bankListRead)
        LOname = input("Name: ")
        LOpin = input("Pin: ")
        for LOdict in readerLogin:
            Account_Balance = int(LOdict["Account_Balance"])
            if LOdict["Name"] == LOname and LOdict["Pin"] == LOpin:
                loggedIN = True
            else:
                print("Wrong user Information,try again")
                login()
    if loggedIN == True:
        print(f"You logged in,Your balance is {Account_Balance}")
    loggedIN = False
    # ADD INFO


login()
