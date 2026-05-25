from expense import Expense


def main():
    print("Running Expense Tracker!")

    expense_file_path = "expenses.csv"


    option = 0

    while option != 3:
        print("*** Expense Tracker ***")
        print("1) Add expense")
        print("2) Check summary")
        print("3) Quit")

        try:
            option = int(input("Choose an option >>> "))
        except ValueError:
            print("Please enter a number from 1 to 3")
            continue

        if option == 1:
            #get user input
            expense = get_user_expense()
            
            #write expenses to a file
            save_expense_to_file(expense, expense_file_path)          
        
        elif option == 2:
            #read file and summarize expenses
            summarize_expense(expense_file_path)
            

        elif option == 3:
            print("Quitting program")

        else:
            print("Invalid option. Please choose from 1 to 3")

    print("Program closed!")


    

def get_user_expense():

    expense_name = input("Enter expense name: ")
    
    expense_categories = ["Food", "Home", "Work", "Fun", "Others"]

    while True:
        print("Select a category: ")
        
        for i, category_name in enumerate(expense_categories):
            print(f"{i+1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        
        try:
            selected_index = int(input(f"Enter a category number {value_range}: ")) - 1
        except ValueError:
            print("Please enter a valid number")
            continue


        if selected_index in range(len(expense_categories)):
            expense_category = expense_categories[selected_index]
            break
        else:
            print("Invalid category. Please try again!")
        
    while True:
        try: 
            expense_amount = float(input("Enter expense amount: "))
            break
        except ValueError:
            print("Please enter a valid amount")
            

    new_expense = Expense(name=expense_name, category=expense_category, amount=expense_amount)

    return new_expense

    


def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"save {expense} to {expense_file_path}")

    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")
    


def summarize_expense(expense_file_path):
    expenses: list[Expense] = []
    
    try:
        with open(expense_file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                expense_name, expense_category, expense_amount = line.strip().split(",")
                line_expense = Expense(name=expense_name, category=expense_category, amount=float(expense_amount))
                expenses.append(line_expense)
    except FileNotFoundError:
        print("No expenses found")
        return


    amount_by_category = {}

    for expense in expenses:
        key = expense.category

        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount



    for key, amount in amount_by_category.items():
        print(f"{key}: {amount:.2f}€")
    
    


if __name__ == "__main__":
    main()