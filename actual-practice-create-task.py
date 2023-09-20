#This code counts the amounts of A, P, or R inputted by the user, which represents aluminum, plastic, or paper trash thrown in a trash bin that can identify their types. However, if the trash thrown in the bin isn't aluminum, paper, or plastic, the trash bin starts melting.#

total_count = {"aluminum": 0, "plastic": 0, "paper": 0}

sortItems = input("What has been collected today? (A, P, or R) ")

def give(sortItems):
    for char in sortItems:
        if char != "A" and char != "P" and char != "R":
            print("YOU HAD TO ENTER A, P, OR R!!! NOW I'M MELTINGGGGG!!!!")
            return False
    return True
count_A = sortItems.count('A')
count_P = sortItems.count('P')
count_R = sortItems.count('R')
#The function is being called on the line under here: Line 17.#
horse_meat = give(sortItems)

total_count["aluminum"] = total_count["aluminum"] + count_A
total_count["plastic"] = total_count["plastic"] + count_P
total_count["paper"] = total_count["paper"] + count_R

if horse_meat:
    print(total_count)