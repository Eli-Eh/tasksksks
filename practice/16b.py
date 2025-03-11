cardNum="8549018035096133"
print(cardNum)

def luhn(cardNum):
    checkingDigit = int(cardNum[-1])
    numlist=list(str(cardNum)[::-1][0: -1])
    sig = 0

    multipliedlist = []
    for i in range(len(numlist)):
        if (i+1)%2==0:
            multipliedlist.append(str(int(numlist[i])*2))
            if int(numlist[i]) > 9:
                str(int(numlist[i * 2]) - 9)
        else:
            multipliedlist.append(numlist[i])

    for i in multipliedlist:
        sig += int(i)

    return (sig+checkingDigit)%2==0

if luhn(cardNum):
    print("valid")
else:
    print("nope")