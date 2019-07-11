# 1
# Creates a dictionary using the keys emotion, location and data, 
# with the correctly associated values from the parameters.
def create_orb(emotion, location, data):
    memory = {'emotion': emotion,'location':location,'data':data}
    return memory

# 2
# Locates the value associated with the key emotion.
def orb_get_emotion(orb):
    return orb['emotion']

# 3
# Changes the value associated with the key emotion.
def change_orb_emotion(orb, new_emotion):
    orb['emotion'] = new_emotion
    return orb

# 4
# Locates the value associated with the key location.
def orb_get_location(orb):
    return orb['location']

# 5
# Changes the value associated with the key location.
def move_orb(orb, new_location):
    orb['location'] = new_location
    return orb

# 6
# Locates the value associated with the key data.
def orb_get_data(orb):
    return orb['data']

# 7
# Creates an empty dictionary.
def create_monster_cast():
    return  {}

# 8
# Adds an entry to monsters, using character as the key and cast_member as the value.
def add_cast_member(monsters, character, cast_member):
    monsters[character] = cast_member
    return monsters

# 9
# Finds the cast member associated with character in monsters. 
def get_cast_member(monsters, character):
    return monsters[character]

# 10
# Calculates the number of characters in monsters.
def get_cast_size(monsters):
    return len(monsters)

# 11
# Changes the value associated with character in monsters to be cast_member. 
# If the character does not already have an entry in monsters, create it.
def change_cast_member(monsters, character, cast_member):
    monsters[character] = cast_member
    return  monsters

# 12
# Checks if character is a key in monsters.
def has_character(monsters, character):
    if character in monsters:
        return True
    else:
        return False

# 13
# Checks if cast_member is a value in monsters.
def has_cast_member(monsters, cast_member):
    if cast_member in monsters.values():
        return True
    else:
        return False

# 14
# Finds the value in the dictionary that is the longest string. 
#You may assume that all cast members will have different length names.
def get_longest_cast_member(monsters):
    longest = ''
    for member in monsters:
        if len(monsters[member]) > len(longest):
            longest = monsters[member]
    return str(longest)

# 15
# Finds the key in the dictionary that is the longest string. 
#You may assume that all characters will have different length names.
def get_longest_character(monsters):
    longest = ''
    for member in monsters:
        if len(member) > len(longest):
            longest = member
    return longest

# 16
#Finds the key in the dictionary that has a value that is the longest string.
# You may assume that all cast members will have different length names.
def get_character_of_longest_cast_member(monsters):
    longest = ''
    for member in monsters:
        if len(monsters[member]) > len(longest):
            longest = monsters[member]
            char = member
    return str(char)



