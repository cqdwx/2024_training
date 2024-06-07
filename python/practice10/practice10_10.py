def count_word(filename, word):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
            count = contents.lower().count(word)
            print(f"The word '{word}' appears {count} times in the file '{filename}'.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

count_word('alice.txt', 'the')
count_word('frankenstein.txt', 'the')