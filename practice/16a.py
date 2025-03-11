# Question 16(a)
# Name and School:

cardNum=int(input("Welcome to CardCheck. Enter your card number: "))
tolerance=3 # tolerance for the amount of attempts one can enter a number for
wrongCount=0 # the amount of wrong attempts for a number entry
blocked = True # wether the user is blocked from access to the service

#converts the number to a string and checks the first character for a 7 or eight
def cardTypeChecker(cardNum):
    match int(str(cardNum)[0]):
        case 7:
            return "a ZincCard"
        case 8:
            return "a WinCard"
        case _:
            return ""

def cvvCalculate(cardNum, expiry):
    cvv=0
    for c in str(expiry):
        cvv+=int(c)
    return (cvv*int(str(cardNum)[0:2]))-int(str(cardNum)[9])

# If the number of wrong attempts is under 3, check whether the length of the number is 16.
# If it is not 16 characters long, increase the amount of wrong attempts and make the user
# re-enter the number. If it is, unblock the user and break the loop.
while wrongCount<tolerance-1:
    if len(str(cardNum))!=16:
        wrongCount+=1
        cardNum = int(input("Invalid number, please try again: "))
    else:
        print("That is correct.")
        blocked = False # This line of code uses a boolean notation (vi)
        break

if blocked:
    print("Too many wrong attempts.")
else:
    expiry=int(input("Enter the card expiry date e.g. 11/26 should be entered as 1126: "))
    print(f"This is {cardTypeChecker(cardNum)}")
    print(f"CVV number: {cvvCalculate(cardNum, expiry)}")
    print(f"Card Number: {str(cardNum)[0:4]}-{str(cardNum)[4:8]}-{str(cardNum)[8:12]}-{str(cardNum)[12:16]} and it is valid")
