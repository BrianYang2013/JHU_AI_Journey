def factorial_str(fact_counter, fact_value):
    output_string = ''

    if fact_counter == 0:      # Base case: 0! = 1
        output_string += '1'
    elif fact_counter == 1:    # Base case: print 1 and result
        output_string += str(fact_counter) +  ' = ' + str(fact_value)
    else:                       # Recursive case
        output_string += str(fact_counter) + ' * '
        next_counter = fact_counter - 1
        next_value = next_counter * fact_value
        ''' Your solution goes here '''
        # output_string += factorial_str(fact_counter-1, fact_value*(fact_counter-1))
        output_string += factorial_str(fact_counter-1, next_value)

    return output_string

user_val = int(input())
print('{}! = '.format(user_val), end="")
print(factorial_str(user_val, user_val))