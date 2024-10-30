def even_numbers(n):
    count = 0
    current_number = 0
    while current_number <= n: # Complete the while loop condition
        if current_number % 2 == 0:
            count = count + 1 # Increment the appropriate variable
        current_number = current_number + 1 # Increment the appropriate variable
    return count
    
print(even_numbers(25))   # Should print 13
print(even_numbers(144))  # Should print 73
print(even_numbers(1000)) # Should print 501
print(even_numbers(0))    # Should print 1

# this program is saying

# while counting up to n by 1 from 0 with current_number, if current number is evenly divisible by 2, increment the count, then increment the current_number to count up by 1