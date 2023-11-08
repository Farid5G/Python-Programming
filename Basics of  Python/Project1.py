# Mini Calculator  
num1 = int(input("Enter the first Number: "))

print("Select the operator:- '+' , '-' , '*' , '/' , '%', '**' ")
operator = input()

num2 = int(input("Enter the second Number: "))

if operator == '+':
    print(f"Addition of number is: {num1 + num2}")
elif operator == '-':
    print(f"Substraction of number is: {num1 - num2}")
elif operator == '*':
    print(f"Multiplication of number is: {num1 * num2}")
elif operator == '/':
    print(f"Divsion of number is: {num1 // num2}")
elif operator == '%':
    print(f"Modulo of number is: {num1 % num2}")
elif operator == '**':
    print(f"Raise to of number is: {num1 ** num2}")
else:
    print("Invalid Operator!!")
