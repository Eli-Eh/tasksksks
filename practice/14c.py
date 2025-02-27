jumps = [5.32, 5.5, 5.39,6.50,6.14]

def bubbleSort(l):
    isNotSorted = True
    temp = 0
    while isNotSorted:
        isNotSorted=False
        for i in range(len(jumps)-1):
            if l[i] > l[i+1]:
                isNotSorted = True
                temp = l[i]
                l[i] = l[i+1]
                l[i+1] = temp
    return l

print(bubbleSort(jumps))