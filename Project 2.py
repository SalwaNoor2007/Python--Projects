#======================================================================================
#  Project    2:          To---Do---List
#======================================================================================

tasks=[]
while True:
    print("\n1. Task add karo")
    print("2. Tasks dekho")
    print("3. Exit")

    choice = input("Number likho: ")

    if choice == "1":
        task = input("Task likho: ")
        tasks.append(task)
        print("Task add ho gaya!")

    elif choice == "2":
        if len(tasks) == 0:
            print("Koi task nahi hai")
        else:
            for task in tasks:
                print("-", task)

    elif choice == "3":
        print("Bye!")
        break

    else:
        print("Galat number")
        