print("\n======================================== Personal Finance Expense Tracker ====================================\n")
program = True
while program == True:
    print("=========================== MENU ========================")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    ch = int(input("\nEnter your choice (1-3): "))
    print("\n==============================================================================================================")

    if ch == 1:
        expense_track = []
        n = int(input("Enter the number of expenses to be added: "))
        for i in range(0,n):
            print(f"\nEntering Expense {i+1}...")
            expense = dict()
            date = input("Enter Date: ")
            expense[f"date"] = date
            category = input("Enter Category: ")
            expense["category"] = category
            description = input("Enter Description: ")
            expense["description"] = description
            print("Entering Amount...")
            print("🧾 NOTE: (Add +ve sign if amount is added and -ve sign if amount is deducted) ")
            amount = float(input("Enter Amount: "))
            expense["amount"] = amount
            expense_track.append(expense)
            print(f"\n {i+1} Expense Added Successfully ✔")

        print(f"\nAdded {n} Expenses Successfully 📜")
            
    elif ch == 2:
        num = len(expense_track)
        if num == 0:
            print("❌ No Expense Records Present, Please Add Expense Records To Continue...")
        else:
            print("📱 Displaying All Expense Records....\n")
            n = 1
            for record in expense_track:
                print(f"{n}) {record}")
                n += 1
            print("\nAll Records Shown Successfully ✔")

    elif ch == 3:
        if num == 0:
            print("❌ No Expense Records Present, Please Add Expense Records To Continue...")
        else:
            print("📖 Getting All Expenses...")
            sum = 0
            n = 1
            for record in expense_track:
                amt = record["amount"]
                print(f"Expense {n}:",amt)
                sum += amt
            print("Total Expense Amount:",sum)
    print("\n===========================================================================================================\n")
    loop = True
    while loop == True:
        cont = input("Want To Continue? (Y/N): ")
        if cont == "N":
            print("\nExiting Program...\n")
            loop = False
            program = False
        elif cont == "Y":
            print("\nRestarting...\n")
            loop = False
            program = True
        else:
            print("\nEnter Valid Choice!!!\n")
            loop = True