import math
def ask():
    n1=97
    n2=122
    while True:
        mid=math.ceil((n1+n2)/2)
        c_char = chr(mid)
        a = input(f"Is your letter >, <, or = {c_char}? ")
        if a == '>':
            n1 = mid + 1
        elif a == '<':
            n2 = mid - 1
        elif a == '=':
            print(f"Your letter is: {c_char}")
            return c_char
        else:
            print("Please enter only '>', '<', or '='.")


def letter():
    c=''
    a=int(input("Enter no of lettres in your word"))
    for i in range (a):
        d=ask()
        c+=d
    print(c)

letter()