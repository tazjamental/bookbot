def get_num_words(book):
    words = book.split()
    num_words = len(words)
    return num_words

def get_character_count(book):
    book_lower = book.lower()
    chars = list(book_lower)
    chars_dict = {}
    for char in chars:
        if char not in chars_dict:
            chars_dict[char] = 1
        elif char in chars_dict:
            chars_dict[char] += 1
    return chars_dict

def dict_sort(to_sort):
    sorted_list = []
    for character in to_sort:
        if character.isalpha():
            count = to_sort[character]
            sorted_list.append({"char": character, "num": count})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(items):
    return items["num"]