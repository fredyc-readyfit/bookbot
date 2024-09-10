def count_words(text = ""):
    words = text.split()
    return len(words)

def count_characters(text = ""):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lowercase_text = text.lower()
    character_dict = {}

    for c in alphabet:
        character_dict[c] = 0

    for c in lowercase_text:
        if c in character_dict:
            character_dict[c] += 1

    return character_dict

def main():
    book = 'books/frankenstein.txt'

    with open(book, 'r') as f:
        file_contents = f.read()

        print(f"--- Begin report of {book} ---")
        words = count_words(file_contents)
        print(f"{words} words found in the document\n")

        characters = count_characters(file_contents)
        for c in sorted(characters.items(), key=lambda x:x[1], reverse=True):
            if c[1] > 0:
                print(f"The '{c[0]}' character was found {c[1]} times")

        print(f"--- End report ---")

main()