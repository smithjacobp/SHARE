def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for groups, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			 user_groups[user] = user_groups.get(user,[]) + [groups]
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

# i need to understand the last line of the function

# it is saying

# key user in dictionary = the value of key user (itself) + the list of groups

# i gues this works because we are iterating through groups as well as users