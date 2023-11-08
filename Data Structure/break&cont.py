names = ["Farid","Fahad","Zaid","Asrar","Aatif","Yahya"]

print(names)

# first print till zaid and rest shouldn't be print exit the loop using break
for name in names:
    if name == "Asrar":
        break
    print(f"using break keyword: {name}")

# skip the name asrar and print rest of all using continue statement

for name in names:
    if name == "Asrar":
        continue
    print(f"using continue keyword: {name}")