#Strings are immutable the functions that are used returns new string  

name = "Farid"

# lowercase and uppercase
print(name.lower())
print(name.upper())

# find() - returns the index value of the particular string if not found return -1
print(name.find('F'))
print(name.find('f')) # case sensitive returns -1

# replace() - replace the string with new characters and returns new string
print(name.replace('Fa','Meh'))

# in - check whether character exit or not returns in boolean
print("Fa" in name)
print("Meh" in name)
