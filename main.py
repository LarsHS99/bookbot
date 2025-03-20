import sys
from stats import get_num_words, get_char_counts, get_sorted_char_counts

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    try:
        book_contents = get_book_text(filepath)
        num_words = get_num_words(book_contents)
        char_counts = get_char_counts(book_contents)
        sorted_char_counts = get_sorted_char_counts(char_counts)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
    
        for i in sorted_char_counts:
            print(f"{i['char']}: {i['count']}")
    except FileNotFoundError:
        print(f"Error: The file at {filepath} could not be found.")
        sys.exit(1)

if __name__ == "__main__":
    main()

