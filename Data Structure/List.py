# list in python is similar to array
print("Lists are mutable i.e changable")
marks = [23,44,23]
print(marks[2]) #print on second index
print(marks[1:3]) #1 is inclusive and 2 is exclusive

# list are mutable i.e changable
# function on list are
marks.append(43) # add at the end  of the list
marks.insert(0,84) #insert on the given index position

# to check whether the element exites or not
print(44 in marks)

# len function returns the length of the list
print(marks)
print(len(marks))

# to  iterate  using  while and for loop
for item in marks:
    print(f"For Loop : {item} ")

i = 0
while (i < len(marks)):
    print(f"While Loop: {marks[i]}")
    i += 1
