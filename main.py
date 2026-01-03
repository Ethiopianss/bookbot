from stats import get_book_text
from stats import character_appearance as char
from stats import sort_dict
import sys
def main():
    # path = "./books/frankenstein.txt"
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    number_words = get_book_text(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(number_words)
    print("--------- Character Count -------")
    characters = char(path)
    # characters.sort(reverse=False, key=sort_on)
    chaar = sort_dict(characters)
    for i in chaar:
        if not i.isalpha():
            continue
        print(f"{i}: {chaar[i]}")
    # print(chaar)
    print("============= END ===============")


main()
