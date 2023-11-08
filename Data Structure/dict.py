# Dictionary stores into key value pairs
salary = {
    "Farid": 93000,
    "Zaid": 30000,
    "Fahad": 9300
}

# to access the new element
# print(f"Salary of Farid is: {salary["Farid"]}")

# to add new element
salary["Asrar"] = 45000

# to reassigned exiting element
salary["Asrar"] = 50000

for sl in salary:
    print(f"Salary of {sl} is: {salary[sl]}")

