#==============================================================================
#    Project    7:        Expence Tracker
#==============================================================================

expenses = []

while True:
    print("\n1. Expense add karo")
    print("2. Sab expenses dekho")
    print("3. Total dekho")
    print("4. Exit")

    choice = input("Choice likho (1-4): ")

    if choice == "1":
        name = input("Kis cheez par kharcha hua? ")
        amount = float(input("Kitne paise? "))
        expenses.append({"name": name, "amount": amount})
        print("Expense add ho gaya!")

    elif choice == "2":
        if len(expenses) == 0:
            print("Abhi koi expense nahi hai.")
        else:
            for item in expenses:
                print(item["name"], "-", item["amount"])

    elif choice == "3":
        total = 0
        for item in expenses:
            total = total + item["amount"]
        print("Total kharcha:", total)

    elif choice == "4":
        print("Bye!")
        break

    else:
        print("Galat choice, dobara try karo.")