print ("Make a simple program with operator +,-,/,* with input type in console terminal")
num1 = int(input("A = "))
num2 = int(input("B = "))
num3 = str(input("Operator = "))
if num3 == ("+") :
    print(num1+num2)
elif num3 == ("-"):
    print(num1-num2)
elif num3 == ("/"):
    print(num1/num2)
elif num3 == ("*"):
    print(num1*num2)
else:
    print("")
    