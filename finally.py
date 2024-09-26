try:
    print("we are performing mathemathical operation of two numbers")
    a=int(input("enter first number: "))
    b=int(input("enter second number: "))
    c=(input("+ for addition, - for substraction, / for division, * for multiplication and / for division \n enter any sign: "))
    match c:
        case '+':
            print("The sum is: ",a+b)
        case '-':
            print("The difference is:  ",a-b)
        case '*':
            print("The multiplication is: ",a*b)
        case '/':
            print("The division is: ",a/b)
        case _ :
            print('invalid input')    
            
except:
    print('error 400')
finally:
    print("Have a great rest of your day")

print("Thank you for using calculator")

