def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_the_words(text):
    #splitting the whole document into words then counting the words instead of characters
    words=text.split()
    return len(words)

def count_the_characters(text):
    lowercase_text = text.lower()
    character_counter_dictionary = {}
    for character in lowercase_text:
        if character in character_counter_dictionary:
            character_counter_dictionary[character] = character_counter_dictionary[character] + 1
        else:
            character_counter_dictionary[character] = 1
    return character_counter_dictionary

def sort_on(items):
    return items["num"]

def creating_a_list(dictionary):
    list_sorting = []
    for characters in dictionary:
        if characters.isalpha():
            list_sorting.append({"char":characters,"num":dictionary[characters]})
    list_sorting.sort(reverse=True, key=sort_on)
    return list_sorting