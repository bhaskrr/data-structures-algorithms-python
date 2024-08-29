# 1. Let us say your expense for every month are listed below,
# 	1. January -  2200
#  	2. February - 2350
#     3. March - 2600
#     4. April - 2130
#     5. May - 2190
#
# Create a list to store these monthly expenses and using that find out,
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

expenses = [2200, 2350, 2600, 2130, 2190]
months = ['January', 'February', 'March', 'April', 'May']

def calculate_extra_expense_in_feb(expense_arr, months_arr):
    extra_expense_in_feb = expenses[months.index('February')] - expenses[months.index('January')]
    return extra_expense_in_feb

def calculate_first_quarter_enpense(expense_arr):
    first_quarter_enpense = 0
    for i in range(3):
        first_quarter_enpense += expense_arr[i]
    return first_quarter_enpense
    
def check_exacly_2000_spent(expense_arr):
    for i in range(len(expense_arr)):
        if expense_arr[i] == 2000:
            return True
    return False
    
def add_month_and_expense(expense_arr, months_arr, month, amount):
    expense_arr.append(amount)
    months_arr.append(month)
    return expense_arr, months_arr
    
expenses, months = add_month_and_expense(expenses, months, 'June', '1980')

def returned_item(expense_arr, months_arr, month, amount):
    expense_arr[months_arr.index(month)] -= amount
    return expense_arr

expenses = returned_item(expenses, months, 'April', 200)
