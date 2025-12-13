expenses=[]  #list to store expense records
print("Welcome to expesne tracker")
while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        date=input("Enter expense date:")
        category=input("Enter type of expense:")
        amount=float(input("Enter expense amount:"))

        expense={
            "date":date,
            "category":category,
            "amount":amount
        }

        expenses.append(expense)
        print(" \nExpense addes")
    elif choice==2:
        if not expenses:
            print("No xpenses record")
        else:
         print( "Your expenses are:")
         for allExpenses in expenses:
            print(f"Date:",allExpenses["date"],",Category:",allExpenses["category"],",Amount:",allExpenses["amount"])
    elif choice==3:
        print("Exiting expense tracker. Goodbye!")
        break



