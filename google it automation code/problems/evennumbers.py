def even_numbers(maximum):

    return_string = "" # Initializes variable as a string

    # Complete the for loop with a range that includes all even numbers
    # up to and including the "maximum" value, but excluding 0.
    for x in range(2, maximum+1, 2):

        # Complete the body of the loop by appending the even number
        # followed by a space to the "return_string" variable.
        return_string = return_string + str(x) + ' '

    # This .strip command will remove the final " " space at the end of
    # the "return_string".
    return return_string.strip() 

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed