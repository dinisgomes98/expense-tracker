from expense import Expense


def main():
    print(f"Running Expense Tracker!")

    expense_file_path = "expenses.csv"

    #get user input
    expense = get_user_expense()
    print(expense)


    #write expenses to a file
    save_expense_to_file(expense, expense_file_path)

    #read file and summarize expenses
    summarize_expense()

    

def get_user_expense():

    expense_name = input("Enter expense name: ")
    
    expense_categories = ["Food", "Home", "Work", "Fun", "Others"]

    while True:
        print("Select a category: ")
        
        for i, category_name in enumerate(expense_categories):
            print(f"{i+1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            expense_category = expense_categories[selected_index]
            break
        else:
            print("Invalid category. Please try again!")
        
    
     
    expense_amount = float(input("Enter expense amount: "))

    new_expense = Expense(name=expense_name, category=expense_category, amount=expense_amount)

    return new_expense

    


def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"save {expense} to {expense_file_path}")

    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name}, {expense.category}, {expense.amount}\n")
    


def summarize_expense():
    print(f"summarize expense")
    


if __name__ == "__main__":
    main()