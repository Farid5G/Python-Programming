s = "Hello How are you I'm learning python programming"

# fp = open("test.txt","w")
# fp.write(s)
# fp.close()

# context manger is the easiest way to write the above program without closing it
with open("text.txt","w") as  fp:
    fp.write(s)