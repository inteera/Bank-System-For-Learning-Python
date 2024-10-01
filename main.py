from User import User
from Customer import Customer
from Admin import Admin


def getUserType():
    return str(input("Enter what user you are\n1 - Admin\n2 - Customer\n> "))

def loginOperations():
    userType = ""
    user = None
    file = None
    fileLines = []

    while True:
        try:
            operation = str(input("Enter what you want to do\n1 - Login\n2 - Sign up\n> "))
            username = str(input("Enter username\n> "))
            password = str(input("Enter password\n> "))
        except:
            print("Invalid input")

        match operation:
            case "1":
                file = open(f"Users/{username}.txt", "r+")
                fileLines = file.readlines()
                if(fileLines[0] == f"u: {username}\n" and fileLines[1] == f"p: {password}\n"):
                    print("Succesfully logged in")
                    userType = str(fileLines[2][3])
                    break
                else:
                    print("Check your credentials")
                    file.close()
            case "2":
                userType = getUserType()
                #TODO check if the user already exists
                file = open(f"Users/{username}.txt", "w+")
                fileLines = file.readlines()
                file.writelines([f"u: {username}\n", f"p: {password}\n", f"t: {userType}\n", f"t: {999999999}\n"])
                break
            case _:
                print("Please enter a valid option")

    match userType:
        case "1":
            user = Admin(username, password)
        case "2":
            user = Customer(username, password)
            user.balance = int(fileLines[3][3:])

    return user

user = loginOperations()

while True:
    try:
        operation = str(input("Enter the operation that you want to do\n1 - Deposit money\n2 - Withdraw money\n3 - Transfer money\n0 - Exit\n> "))
        if(operation != "0"):
            amount = int(input("Enter the amount (between 0 and 100,000)\n> "))
            if(amount < 0 or amount > 1000000):
                ValueError
    except:
        print("Please enter a valid number between 0 and 100,000")
            
    match operation:
        case "1":
            user.balance += amount
            print(f"Your balance now: {user.balance}")
        case "2":
            if(user.balance >= amount):
                user.balance -= amount
                print(f"Your balance now: {user.balance}")
            else:
                print(f"Please enter a value that is same or less than your balance ({user.balance})")
        case "3":
            toTransfer = input("Who to transfer\n> ")
            #TODO Transfer logic
        case "0":
            break

#TODO save to file

