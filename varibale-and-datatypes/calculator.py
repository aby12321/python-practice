a = int(input("value of a is"))
b = int(input("value of b is"))
c = input("+ = 1 ,/ = 2 ,- = 3 ,// = 4 ,* = 5")

if (c == "1") :
    print(a+b)

elif (c == "2") :
    print(a/b)

elif (c == "3") :
    print(a-b)

elif (c == "4") :
    print(a//b)

elif (c == "5") :
    print(a*b)

else :
    print("Invalid......")