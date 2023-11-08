print("Tuples are immutable not changable")
marks = (34,65,98,98,98)
print(marks)

# marks[0] = 87 Error we cannot change or assign in tuple 
# two major function are count and index
print("Number is 98")
print(f"This function returns the count of the given number in tuple: {marks.count(98)}")

print("Number is 65")
print(f"This function return the index of the number in the tuple: {marks.index(65)}")

# to make tuple () are not necessary you can directly assign multiple value and by 
# default it is a tuple
name = "Farid","Zaid","Fahad"
print(name) #bydefault it is tuple