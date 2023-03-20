def getFactorial(number:int) -> int:
    if number == 0:
        return 1
    return number * getFactorial(number - 1)

def combination(num1: int, num2:int) -> int:
    numberator = getFactorial(num2)
    third = num2 - num1
    denominator = (getFactorial(third) * getFactorial(num1))
    return (numberator/denominator)



while True:
    choice = int(
        input("What do you want to calculate: \n1. Factirial\n2. Combination\n\nType here: "))
    if(choice == 1):
       num = int(input("Enter the number for which you want factorial: "))
       print(f'Factorial of {num} is : {getFactorial(num)}')
       print("")

    elif (choice == 2):
       num1 = int(input("Combination of which number: "))
       num2 = int(input("In what of which number: "))
       print(
           f'The combination of {num1} in {num2} is equal to = {int(combination(num1, num2))}')
       print("")



