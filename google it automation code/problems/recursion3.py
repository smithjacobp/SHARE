def sum_positive_numbers(n):
  if n == 0:
    return n
  return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

# if the base case where the loop stop occurs, which is at 0, return n

# otherwise return n + itself - 1 put into the function, which is just adding the new n each time

