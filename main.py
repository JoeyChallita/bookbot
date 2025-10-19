from stats import count_words, character_count, sort_dict
import sys

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    string_text = get_book_text(book_path)
    print("----------- Word Count ----------")
    print(f"Found {count_words(string_text)} total words")
    print("--------- Character Count -------")
    char_count = character_count(string_text)
    sort_d = sort_dict(char_count)
    for char in sort_d:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")


main()