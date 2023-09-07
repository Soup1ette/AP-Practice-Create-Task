toDoList = ["Math Homework", "Cook Dinner", "Fold Laundry"]

def delItem(item):
   if toDoList.count(item) == 0:
      print("ERROR")
      return -1
   toDoList.remove(item)
   return toDoList

def addItem(item):
   toDoList.append(item)
   return toDoList
   
userAns = input("Do you want to add to your list or quit? A/Q/D")
while userAns == "A":
   item = input("What item do you want to add?")
   addItem(item)
   if userAns == "D":
      item = input("What item do you want to remove?")
      deleteItem(item)
   userAns = input("Do you want to add to your list or quit? A/Q/D")


print(toDoList)