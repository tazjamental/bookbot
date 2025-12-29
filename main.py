import sys
from stats import get_num_words, get_character_count, dict_sort

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("Usage: python3 main.py <path_to_book>")
    if len(sys.argv) <= 1:
        print(" Filename missing")
        sys.exit(1)
    book_path = sys.argv[1]
    book = get_book_text(book_path)
    num_words = get_num_words(book)
   
    character_count = get_character_count(book)
    sorted_dictionary = dict_sort(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for line in sorted_dictionary:
        char = line["char"]
        num = line["num"]
        print(f"{char}: {num}")
    print("============= END ===============")
    

main()