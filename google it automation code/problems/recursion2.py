def count_users(group):
  count = 0
  for member in get_members(group):
    if is_group(member):
      count += count_users(member)
    else:
      count += 1
  return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18


# this is out of order and uses functions which are not defined here but must be defined elsewhere or the code would not work

# this program is saying

# add 1 to the count as the base case

# otherwise, for each member of each group if they exist, add those members to the count by the function calling itself and adding 1




