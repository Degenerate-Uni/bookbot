import sys
from stats import get_word_count
from stats import get_character_count
from stats import sorted_dict

def get_book_text(path_to_book):
    # Function to read the content of a book file
    with open(path_to_book) as book:
        text = book.read()   
    return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    else:
        text = get_book_text(sys.argv[1])
        char_count = get_character_count(text)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(f"Found {get_word_count(text)} total words.")
        print("---------- Character Count -------")
        for char in sorted_dict(char_count):
            print(f"{char['char']}: {char['num']}")
        print("============= END ===============")

main()