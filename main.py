FILE_PATH = "books/frank.txt"


def count_words(text):
    return len(text.split())


def count_letters(text):
    letters_map = {}

    for letter in text.lower():
        if letter in letters_map:
            letters_map[letter] += 1
        else:
            letters_map[letter] = 1

    return letters_map


def print_report(file_path, words_count, letters_map):
    print(f"\n--- Begin report of {file_path} ---\n")

    print(f"{words_count} words found in the document\n")

    letters = list(letters_map)
    letters.sort()
    for letter in letters:
        if not letter.isalpha():
            continue

        print(f"The {letter} character was found {letters_map[letter]} times")

    print("\n--- End report ---")


with open(FILE_PATH) as f:
    file_contents = f.read()

print_report(FILE_PATH, count_words(file_contents), count_letters(file_contents))
