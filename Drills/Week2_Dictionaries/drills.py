# drill 1
#In this exercise, your function will receive no parameters. It will create an empty dictionary and return it.
def empty_dictionary():
	return {}

# drill 2
#In this exercise your function will receive no parameters. It will create a dictionary where the keys are the names of states in the U.S., and the values are the names of the state trees. The must be completed for the states: Texas, Utah, and Vermont. Their state trees are Pecan, Quaking Aspen, and Sugar Maple, respectively.
def fixed_dictionary():
    new = {
    "Texas": "Pecan",
    "Utah": "Quaking Aspen",
    "Vermont": "Sugar Maple"}
    return new

# drill 3
#In this exercise your function will receive two parameters. The first is a list of strings to use as keys in a dictionary. The second is a list of values to use with the keys. The function will create a dictionary with every key/value pair from the lists. It will then return the dictionary
def lists_to_dict(keys, values):
    List = {}
    for i in range(len(keys)):
        List[keys[i]] = values[i]
    return List

# drill 4
#In this exercise your function will receive four parameters. These parameters correspond to statistics for a baseball player's trading card. The function will use these parameters for values in a dictionary. The keys for each value are specified below. Finally, the function will return the dictionary constructed with these values.
def values_to_dict(at_bats, hits, runs_batted_in, batting_average):
    return {'AB':at_bats,'H':hits,'RBI':runs_batted_in,'AVG':batting_average}

# drill 5
#In this exercise, your function will receive 2 parameters, a dictionary, and string that is a key in the dictionary. The function will find and return the value associated with the key.
def get_dict_value01(dictionary, key):
    return dictionary[key]

#drill 6
#In this exercise, your function will receive 3 parameters, a dictionary, a string that is a key in the dictionary, and a string value. The function will update the value associated with the key in the dictionary to the value in the third parameter. It will then return the dictionary.
def change_dict_value01(dictionary, key, new_value):
    dictionary[key] = new_value
    return dictionary

# drill 7
#In this exercise, your function will receive 3 parameters, a dictionary, a string that will be a key in the dictionary, and a string value. The function will add the new key and value to the dictionary. It will then return the dictionary.
def add_dict_value01(dictionary, new_key, new_value):
    dictionary[new_key] = new_value
    return dictionary

# drill 8
#In this exercise, your function will receive 2 parameters, a dictionary, and string that is a key in the dictionary. The function will find and return the value associated with the key.
def get_dict_value02(dictionary, key):
    return dictionary[key]

# drill 9
#In this exercise, your function will receive 3 parameters, a dictionary, a string that is a key in the dictionary, and a string value. The function will update the value associated with the key in the dictionary to the value in the third parameter. It will then return the dictionary.
def change_dict_value02(dictionary, key, new_value):
    dictionary[key] = new_value
    return dictionary

# drill 10
#In this exercise, your function will receive 3 parameters, a dictionary, a string that will be a key in the dictionary, and a string value. The function will add the new key and value to the dictionary. It will then return the dictionary.
def add_dict_value02(dictionary, new, val):
    dictionary[new] = val
    return dictionary
