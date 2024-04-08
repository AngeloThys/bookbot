def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = get_num_words(text)
    chars = get_char_count(text)
    chars_ordered = dict_to_list(chars)

    print(f"--- The beginning of {book_path}'s report ---")
    print(f"It contains {num_words}!")
    print("The number of each character is as follows:")
    for char in chars_ordered:
        print(f"{char['value']} times {char['key']}")
    print(f"--- End report of {book_path} ---")
    print("Enjoy!")


def sort_on(d):
    return d["value"]


def dict_to_list(d):
    new_list = []

    for key, value in d.items():
        new_list.append({"key": key, "value": value})

    new_list.sort(reverse=True, key=sort_on)

    return new_list


def get_text(book_path):
    with open(book_path) as f:
        return f.read()


def get_num_words(text):
    return len(text.split())


def get_char_count(text):
    words = text.split()
    string = "".join(words)
    string_lowercase = string.lower()
    chars = {}

    for char in string_lowercase:
        if char.isalpha():
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1

    return chars


main()
