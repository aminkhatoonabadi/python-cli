def calculate(num1,num2,opt):
    if opt == "+":
        return num1+num2
    elif opt == "-":
        return num1-num2
    elif opt == "*":
        return num1*num2
    elif opt == "/":
        if num2 == 0:
            return "You cant divide number by Zero(0)"
        else:
            return num1/num2
    elif opt == "%":
        if num2 == 0:
            return "You cant divide number by Zero(0)"
        else:
            return num1%num2
    elif opt == "**":
        return num1**num2
    elif opt == "//":
        return num1//num2
print("Welcome To Amin's Calculator")
while True:
    print("------------------------------")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exponentiation (**)")
    print("7. Floor division (//)")
    print("8. Exit Program")
    print()
    while True:
        opt = input("Please select an option: ")
        Operators = ["+","-","*","/","%","**","//"]
        if opt == "1" or opt == "2" or opt == "3" or opt == "4" or opt == "5" or opt == "6" or opt == "7":
            opt =  Operators[int(opt)-1]
            break
        elif opt == "8" or opt == "Exit":
            exit()
        else:
            print("Your option us not valid!")
    while True:
        try:
            num1= float(input("Enter first number: "))
            break
        except ValueError:
            print("Please enter real numbers only...")  
            continue
    while True:
        try:
            num2= float(input("Enter second number: "))
            break
        except ValueError:
            print("Please enter real numbers only...")  
            continue
    result = (calculate(num1,num2,opt))
    print("{0} {1} {2} = {3}".format(num1,opt,num2,result))
    while True:
        cont = input("Do you want to continue using calculator? (type Yes OR Y if you want to continue and No OR N for Exit): ")
        if cont == "No" or cont == "no" or cont == "N" or cont == "n":
            exit()
        elif cont == "Yes" or cont == "yes" or cont == "Y" or cont == "y":
            break
        else:
            print("Your selection is not valid!")