def endangered_animals(animal_dict):
    result = ""
    # Complete the for loop to iterate through the key and value items 
    # in the dictionary.    
    for k, v in animal_dict.items(): 
        # Use a string method to format the required string.
        result += f"{k}\n"
    return result


print(endangered_animals({"Javan Rhinoceros":60, "Vaquita":10, "Mountain Gorilla":200, "Tiger":500}))

# Should print:
# Javan Rhinoceros
# Vaquita
# Mountain Gorilla
# Tiger

# used a literal with a new line as a format to print out dictionay keys in a vertical list