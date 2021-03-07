import datetime
import time
import fileinput
import re
import sys

x = datetime.datetime.now()
t = x.strftime("%c")

class User:
    c_id = ""

    def __init__(self, name="", surname="", ID=""):
        self.name = name
        self.surname = surname
        self.ID = ID
        self.email = self.name + "." + self.surname + "@csbank.com"
        self.data_list = self.read_txt('bankdata.txt')
        self.balance_list = self.read_txt('balance.txt')

    def login(self, liste):
        while True:
            try:  # 2 bilginin dogru girilmesiye birlikte User sinifi menusu calisir.
                print('\t'.expandtabs(44), 20*'='+" WELCOME, Please LOGIN first "+20*'=')
                print()
                self.name = input("\t\t\t Enter a current customer NAME: ")
                self.ID = input("\t\t\t Enter a current customer ID: ")
                if len(self.name) > 2 and len(self.ID) > 2:
                    print("--> LOADING |||||||||||", end='')
                    for i in range(3):
                        print("|||||||"*i,end='')
                        time.sleep(1)
                    break
            except:
                print("You have to enter least 3 digit!")

        for i in liste:
            if i[0] == self.ID and i[1] == self.name:
                print("\nWelcome {}, \nLogin is successful!".format(self.name).upper())
                User.c_id = self.ID  # login olan kullanicinin ID si class variable a atandi.
                self.main_menu(i)
        else:
            print("---> Invalid user name or ID! Try again <---")

    def create_user(self):
        while True:
            try:
                print("You have to enter least 3 digit!")
                self.name = input("Enter a NAME: ")
                self.surname = input("Enter a SURNAME: ")
                self.ID = input("Enter a ID No: ")
                Bank.balance = int(input("The amount of money deposited:"))
                self.email = self.name + "." + self.surname + "@csbank.com"
                if len(self.ID) > 2 and len(self.name) > 2:
                    break
            except:
                print("You have to enter least 3 digit!")

        with open("bankdata.txt", "r+") as f:
            for line in f:
                line = line.rstrip()
                nesne1 = re.search(self.ID, line)
                nesne2 = re.search(self.name, line)
                if nesne1 and nesne2:
                    print("Sorry! This NAME and ID are in use.")
                    break
            else:
                f.write(self.ID + "\t\t")
                f.write(self.name + "\t\t")
                f.write(self.surname + "\t\t")
                f.write(self.email + "  \n")
                f.seek(0)

            with open("balance.txt", "r+") as text:
                for line in text:
                    line = line.rstrip()
                text.write(self.ID + "\t\t")  # user class tan alinan musteri numarasini txt ye yazdim.
                text.write(str(Bank.balance) + "\t\t")  # mevcut balans i txt ye yazdim.
                text.write(t + " \n")  # islem tarihini txt ye yazdim.
                print("Registration is done! \nYou must have again login..")
                exit()

    def read_txt(self, file):
        f = open(file, 'r')
        lines_list = []
        for line in f:
            line = line.rstrip().split("\t\t")
            lines_list.append(line)
        return lines_list  # lines_list = musteri bilgileri listelerinin listesi

    def fileInput(self, searchExp, replaceExp):
        for line in fileinput.input('bankdata.txt', inplace=1):
            if searchExp in line:
                line = line.replace(searchExp, replaceExp)
            sys.stdout.write(line)

    def edit_user(self, liste):  # liste = musteri bilgileri listelerinin listesi
        for i in liste:
            if i[0] == self.ID and i[1] == self.name:
                print(i)
                print("Customer found!")
                q = int(input("Which information will be updated? \nNAME    --> 1, \nSURNAME --> 2 \ne-mail  --> 3 \nChoice:.."))
                if q == 1:
                    new_name = input("Enter a NEW name:")
                    self.fileInput(i[1], new_name)
                    print("The name has been changed \nYou must have again login..")
                    User.logout(self)
                if q == 2:
                    new_surname = input("Enter a NEW surname:")
                    self.fileInput(i[2], new_surname)
                    print("The surname has been changed \nYou must have again login..")
                    User.logout(self)
                if q == 3:
                    new_email = input("Enter a NEW email:")
                    self.fileInput(i[3], new_email)
                    print("The mail has been changed \nYou must have again login..")
                    User.logout(self)
                else:
                    break

    def start(self):
        if len(self.data_list) == 0:
            self.data_list.append(['111', 'ali', 'can', 'ali.can@csbank.com'])
            self.data_list.append(['222', 'semih', 'can', 'semih.can@csbank.com'])
            self.data_list.append(['333', 'cabir', 'can', 'cabir.can@csbank.com'])
        self.login(self.data_list)

    def logout(self):
        print("{} quit the application..".format(self.name).upper())
        exit()

    def delete_user(self):
        f = open("bankdata.txt", "r+")
        n = open("bankdata2.txt", "w+")
        self.name = input("Enter customer NAME to be deleted: ")
        self.surname = input("Enter customer SURNAME to be deleted: ")
        self.ID = input("Enter customer ID to be deleted: ")
        for line in f:
            nesne1 = re.search(self.name, line)
            nesne2 = re.search(self.ID, line)
            if nesne1 and nesne2:
                print("Your account is DELETED! ")
                continue
            else:
                n.write(line)
        f = open("bankdata.txt", "w")  # ilk dosyanin icini sildim.
        with open("bankdata2.txt", "r+") as n:
            with open("bankdata.txt", "w+") as f:
                for line in n:
                    f.write(line)

    def main_menu(self, liste):
        while True:
            menu = ["===== Welcome to C&S Bank =====",
                    " NEW Customer           ---> 1",
                    " Edit Customer Information-> 2",
                    " Delete Customer Account --> 3",
                    " Transaction_menu       ---> 4...",
                    " Logout             -------> 5"]
            for i in menu:
                print('\t'.expandtabs(44), i)
            print("ID: {}\nName: {}\nSurname: {}\nMail: {}\n".format(liste[0], liste[1], liste[2], liste[3]))
            choice = input("Enter your choice:...")
            if choice == "1":
                u.create_user()  # User class in create_user() methodu calisir.
            elif choice == "2":
                u.edit_user(self.data_list)  # User class in edit_user() methodu calisir.
            elif choice == "3":
                u.delete_user()  # User class in delete_user() methodu calisir.
            elif choice == "4":
                Bank.transaction_menu(self)  # Bank class in transaction_menu() methodu calisir.
            elif choice == "5":
                u.logout()  # User class in logout() methodu calisir.
            else:
                print("Something went wrong. Try again later..")

class Bank(User):
    c_balance = 0

    def __init__(self, balance='', owner=''):
        super().__init__()
        self.owner = owner
        self.balance = balance

    def fileInput(self, searchExp, replaceExp):
        for line in fileinput.input('balance.txt', inplace=1):
            if searchExp in line:
                line = line.replace(searchExp, replaceExp)
            sys.stdout.write(line)

    def getBalance(self, liste):
        for i in liste:
            if i[0] == User.c_id:
                Bank.c_balance = int(i[1])
                print("your balance: {} \nLast transaction date: {}".format(Bank.c_balance, i[2]))

    def deposit(self, liste):
        for i in liste:
            if i[0] == User.c_id:
                amount = int(input("Enter the amount to DEPOSIT: "))
                Bank.c_balance = int(i[1])
                Bank.c_balance += amount
                Bank.c_balance = str(c.c_balance)
                self.fileInput(i[1], Bank.c_balance)
                print("\nYour current BALANCE is:", Bank.c_balance)
                u.logout()

    def withdraw(self, liste):
        for i in liste:
            if i[0] == User.c_id:
                amount = int(input("Enter the amount to WITHDRAW: "))
                Bank.c_balance = int(i[1])
                if Bank.c_balance >= amount:
                    Bank.c_balance -= amount
                    Bank.c_balance = str(Bank.c_balance)
                    self.fileInput(i[1], Bank.c_balance)
                    print("\nYour current BALANCE is:", Bank.c_balance)
                    u.logout()
                else:
                    print("\nBalance is insufficient  ")
                    print("\nYour current BALANCE is:", Bank.c_balance)

    def transfer(self, liste):
        for i in liste:
            if i[0] == User.c_id:
                Bank.c_balance = int(i[1])  # login olan kullanicinin balans i class variable a atandi.
                print("You have", Bank.c_balance, '$')
        id_number = input("Enter the ID of Customer to be transferred: ")
        if id_number != User.c_id:
            for i in liste:
                if i[0] == id_number:
                    print("Client has been found")
                    break
            try:
                amount = int(input("Enter the AMOUNT to transfer: "))
                if Bank.c_balance >= amount:
                    Bank.c_balance -= amount
                    Bank.c_balance = str(Bank.c_balance)
                    for i in liste:
                        if i[0] == User.c_id:
                            self.fileInput(i[1], Bank.c_balance)
                        if i[0] == id_number:
                            result = int(i[1]) + amount
                            result = str(result)
                            self.fileInput(i[1], result)
                    print("Transfer done! \nYou must have again login..")
                    exit()
                else:
                    print("\nBalance is insufficient  ")
                    print("\nYour current balance is:", self.balance)
                    Bank.transaction_menu(self.balance_list)
            except ValueError:
                print("The input was not a valid amount.")
        else:
            print("Error! Both the same account number..\nExits the application.")
            exit()

    def transaction_menu(self):
        while True:
            menu = ["====== Transaction Menu ======",
                    " Get Balance       -------> 1",
                    " Deposit Money     -------> 2",
                    " Withdraw          -------> 3",
                    " Transfer Money    -------> 4",
                    " Back to Main Menu -------> 5...",
                    " Logout            -------> 6"]
            for i in menu:
                print('\t'.expandtabs(55), i)
            choice = input("Enter your choice:...")
            c = Bank()
            if choice == "1":
                c.getBalance(self.balance_list)
            elif choice == "2":
                c.deposit(self.balance_list)
            elif choice == "3":
                c.withdraw(self.balance_list)
            elif choice == "4":
                c.transfer(self.balance_list)
            elif choice == "5":
                for i in self.data_list:
                    if i[0]==Bank.c_id:
                        User.main_menu(self,i)
            elif choice == "6":
                u.logout()
            else:
                print("Something went wrong. Try again Please...")
u = User()
c = Bank()
u.start()
