# words = ["hello", "hey", "goodbye", "yo", "yes"]
# for word in words:
#     print(word.upper())


def print_upper_words(words):
    """Print each word in a list on a separate line, in all uppercase."""

    for word in words:
        print(word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])


def print_upper_words_starting_with_e(words):
    """Print words in the list that start with the letter 'e', in all uppercase."""

    for word in words:
        if word.lower().startswith("e"):
            print(word.upper())


print_upper_words_starting_with_e(["apple", "Elephant", "orange", "Exit"])


def print_upper_words_starting_with_set(words, letters):
    """Print words in the list that start with any of the given letters, in all uppercase."""

    for word in words:
        if word.lower().startswith(tuple(letters)):
            print(word.upper())


print_upper_words_starting_with_set(["apple", "Elephant", "orange", "Exit"], {"e", "o"})
