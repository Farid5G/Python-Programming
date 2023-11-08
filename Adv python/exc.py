# try catch is used to handle Exception so that our program doesn't stop or fail

try:
    num = int(input("Enter the number to add with 4: "))
    print(num + 4)
except Exception as e:
    print("Some error occured: ",e)