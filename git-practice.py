toDoList = ["Math Homework", "Cook Dinner", "Fold Laundry"]

def addItem(item):
   # Finish this code
   return toDoList

userAns = input("Do you want to add to your list or quit? A/Q")
while userAns == "A":
   item = input("What item do you want to add?")
   addItem(item)
   userAns = input("Do you want to add to your list or quit? A/Q")
