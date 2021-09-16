# Returns number of pennies if pennies are doubled num_days times
def double_pennies(num_pennies, num_days):
    total_pennies = 0

    ''' Your solution goes here '''

    if (num_days) == 0: 
        total_pennies = num_pennies

    else:
        total_pennies = double_pennies((num_pennies * 2), (num_days - 1))

    return total_pennies

# Program computes pennies if you have 1 penny today,
# 2 pennies after one day, 4 after two days, and so on
starting_pennies = int(input("Starting Pennies: "))
user_days = int(input("After # Days: "))

print('Number of pennies after', user_days, 'days: ', end="")
print(double_pennies(starting_pennies, user_days))