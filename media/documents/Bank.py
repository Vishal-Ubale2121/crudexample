import pickle
import os
import pathlib
import time


class Account:
    accNo = 0
    name = ''
    deposit = 0
    type = ''

    def createAccount(self):
        self.accNo = int(input("Enter the account no : "))
        self.name = input("Enter the account holder name : ")
        self.type = input("Enter the type of account [C/S] : ")
        self.deposit = int(input("Enter The amount(>=500 for Saving and >=1000 for current Account:"))
        print("\n\n\nAccount Created Successfully")

    def showAccount(self):
        print("Account Number : ", self.accNo)
        print("Account Holder Name : ", self.name)
        print("Type of Account", self.type)
        print("Balance : ", self.deposit)

    def modifyAccount(self):
        print("Account Number : ", self.accNo)
        self.name = input("Modify Account Holder Name :")
        self.type = input("Modify type of Account :")
        self.deposit = int(input("Modify Balance :"))

    def depositAmount(self, amount):
        self.deposit += amount

    def withdrawAmount(self, amount):
        self.deposit -= amount

    def report(self):
        print(self.accNo, " ", self.name, " ", self.type, " ", self.deposit)

    def getAccountNo(self):
        return self.accNo

    def getAcccountHolderName(self):
        return self.name

    def getAccountType(self):
        return self.type

    def getDeposit(self):
        return self.deposit




def intro():
    print("##########################################################################################################")
    print("************************************ HARMAN CORPORATE BANK PVT.LTD **************************************")
    time.sleep(0.5)
    print("Welcome to online Banking System")
    time.sleep(0.5)
    print("Press Enter to continue...")
    input()


def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)


def displayAll():
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        for item in mylist:
            print(item.accNo, " ", item.name, " ", item.type, " ", item.deposit)
        infile.close()
    else:
        print("No records to display")


def displaySp(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist:
            if item.accNo == num:
                print("Your account Balance is = ", item.deposit)
                found = True
    else:
        print("No records to Search")
    if not found:
        print("No existing record with this number")


def depositAndWithdraw(num1, num2):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist:
            if item.accNo == num1:
                if num2 == 1:
                    amount = int(input("Enter the amount to deposit : "))
                    item.deposit += amount
                    print("Your account is updted")
                elif num2 == 2:
                    amount = int(input("Enter the amount to withdraw : "))
                    if amount <= item.deposit:
                        item.deposit -= amount
                    else:
                        print("You cannot withdraw larger amount")

    else:
        print("No records to Search")
    outfile = open('newaccounts.data', 'wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')


def deleteAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist:
            if item.accNo != num:
                newlist.append(item)
        os.remove('accounts.data')
        outfile = open('newaccounts.data', 'wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')


def modifyAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist:
            if item.accNo == num:
                item.name = input("Enter the account holder name : ")
                item.type = input("Enter the account Type : ")
                item.deposit = int(input("Enter the Amount : "))

        outfile = open('newaccounts.data', 'wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')


def writeAccountsFile(account):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else:
        oldlist = [account]
    outfile = open('newaccounts.data', 'wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')


ch = ''
num = 0
intro()

while ch != 8:

    print("##########################################################################################################")

    print("\t\t\t\t\t\t\t\t\tMAIN MENU")
    print("\t\t\t\t\t\t\t\t\t1. NEW ACCOUNT")
    print("\t\t\t\t\t\t\t\t\t2. DEPOSIT AMOUNT")
    print("\t\t\t\t\t\t\t\t\t3. WITHDRAW AMOUNT")
    print("\t\t\t\t\t\t\t\t\t4. BALANCE ENQUIRY")
    print("\t\t\t\t\t\t\t\t\t5. ALL ACCOUNT HOLDER LIST")
    print("\t\t\t\t\t\t\t\t\t6. CLOSE AN ACCOUNT")
    print("\t\t\t\t\t\t\t\t\t7. MODIFY AN ACCOUNT")
    print("\t\t\t\t\t\t\t\t\t8. EXIT")
    print("##########################################################################################################")
    print("Enter number to select Menu:")
    ch = input()

    print("\tEnter your choice:",ch)

    if ch == '1':
        writeAccount()
    elif ch == '2':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num, 1)
    elif ch == '3':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num, 2)
    elif ch == '4':
        num = int(input("\tEnter The account No. : "))
        displaySp(num)
    elif ch == '5':
        displayAll()
    elif ch == '6':
        num = int(input("\tEnter The account No. : "))
        deleteAccount(num)
    elif ch == '7':
        num = int(input("\tEnter The account No. : "))
        modifyAccount(num)
    elif ch == '8':
        print("\tThanks for using Harman online bank systems.")
        break
    else:
        print("Invalid choice")

ch = input("Enter your choice : ")














