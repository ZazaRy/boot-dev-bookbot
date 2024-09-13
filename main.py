book = 'frankenstein.txt'
with open(book, 'r') as file:
    file_contents = file.read()

    count = 0
    words = file_contents.split()
    word_count = len(file_contents.split())

def letters(book: str) -> dict:
    letter_count = {}
    for letter in book:
        letter_count[letter] = letter_count.get(letter, 0)+1
    return letter_count


def convert_to_list(counts: dict) -> list:
    lst = []
    for letter, count in counts.items():
        if letter.isalpha():
            lst.append({"letter": letter, "count": count})
    return lst

def print_em(counts, word_count, book):
    print(f"-----Data for the book {book}-----")
    print(f"{word_count} words found in the document")

    counts.sort(key=lambda x: x["count"], reverse=True)

    for item in counts:
        print(f"The '{item["letter"]}' character was found {item["count"]} times")

    print("-----End of report-----")


letter_counts = letters(file_contents.lower())
converted = convert_to_list(letter_counts)
print_em(counts=converted, word_count=word_count, book=book)
