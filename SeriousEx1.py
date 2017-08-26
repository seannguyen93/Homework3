items = ["T-shirt","Sweater"]
loop_continue = True
choice = str(input("Welcome to our shop, what do you want (C, R,U,D)?"))
def print_item():
    item_no = 1
    for item in items:
        print ("Our items")
        print(item_no, end=".")
        print (item)
        item_no += 1
    if choice == "C":
        new_item = input ("Enter yo item bro")
        items.append(new_item)
        print(items)
    elif choice == "R":
        print (items)
    elif choice == "U":
        position = int(input("Update yo item babe"))
        new_item_name = input ("Enter yo fuking item babe")
        items [position - 1] = new_item_name
    elif choice == "D":
        position int(input("Enter position u want to delete"))
        items.pop (position-1)
        item_no = 1
        for item in items:
            print ("#", end="")
            print (item_no, end=".")
            print (item)
            item_no += 1
    else:
        print ("See yo biatch")
        loop_continue = False