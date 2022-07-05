# myfile = open("Dishes database.txt", "r")
# mylist = myfile.readlines()
# z = []
# for i in mylist:
#     i = i.split("\n")[0]
#     z.append(i)
# print(z)
# myfile.close()

# import pickle

# my_dict = "你好吗"

# with open('my_dict.pickle', 'wb') as f:
#     pickle.dump(my_dict, f)

# with open('my_dict.pickle', 'rb') as f:
#     my_dict_unpickled = pickle.load(f)

# print(my_dict_unpickled)

from tkinter import *

def close_window():
  global running
  running = False  # turn off while loop
  print( "Window closed")

root = Tk()
root.protocol("WM_DELETE_WINDOW", close_window)
cv = Canvas(root, width=200, height=200)
cv.pack()

running = True
# This is an endless loop stopped only by setting 'running' to 'False'
while running: 
  for i in range(200): 
    if not running: 
        break
    cv.create_oval(i, i, i+1, i+1)
    root.update() 