def get_word_count(text):
    # Function to count the number of words in a text
    words = text.split()
    return len(words)

def get_character_count(text):
    # Function to count the number of characters in a text
    character = {}
    for char in text:
        if char.lower() in character: 
            character[char.lower()] += 1
        else:
            character[char.lower()] = 1
    
    return character

def sort_on(dict):
    return dict["num"]

def sorted_dict(dict):
    sorted_list =[]
    # Function to sort a dictionary by its values
    for char, num in dict.items():
        if char.isalpha():
            new_dict = {}
            new_dict["char"] = char
            new_dict["num"] = num
            sorted_list.append(new_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list