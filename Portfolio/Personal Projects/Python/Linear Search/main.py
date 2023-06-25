myArr = []
for i in range(2, 21, 2):
    myArr.append(i)


def linear_search():
    found = False
    while found == False:
        item = int(input("Please enter item to be found: "))

        for i in range(len(myArr)):
            if myArr[i] == item:
                found = True

        if found == True:
            print("Item found")
        else:
            print("Item not found")

linear_search()