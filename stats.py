def get_num_words(book_contents):
    num_words = len(book_contents.split())
    return num_words

def get_char_counts(book_contents):
    char_counts = {}
    book_contents = book_contents.lower()

    for char in book_contents:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def get_sorted_char_counts(char_counts):
    sorted_chars = [
        {"char": char, "count": count}
        for char, count in char_counts.items()
        if char.isalpha()
    ]

    sorted_chars.sort(key=lambda x: x["count"], reverse=True)

    return sorted_chars