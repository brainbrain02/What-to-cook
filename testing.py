myfile = open("Dishes database.txt", "r")
mylist = myfile.readlines()
z = []
for i in mylist:
    i = i.split("\n")[0]
    z.append(i)
print(z)
myfile.close()