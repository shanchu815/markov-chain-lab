"""Generate Markov text from text files."""

import sys
from random import choice


def open_and_read_file(filepath):
    """Take file paths as a list of strings; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text = ''
    for file in filepath:
        text_file = open(file)
        text = text + text_file.read()
        text_file.close()

    return text


def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita', 2)

    Each bigram will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'juanita'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()

    words.append(None)

    for i in range(len(words) - n):
        key = tuple(words[i:i + n])
        value = words[i + n]

        if key not in chains:
            chains[key] = []

        chains[key].append(value)

        # or we could replace the last three lines with:
        #    chains.setdefault(key, []).append(value)

    return chains


def make_text(chains):
    """Return text from chains."""

    # To check a value ends in punctuation.
    punct = (['.', '?', '!'])

    keys = list(chains.keys())

    key = choice(keys)

    # Check if the first character of the first item in the key is uppercase
    while not key[0][0].isupper():
        key = choice(keys)

    words = list(key)
    word = choice(list(chains[key]))

    while word is not None:
        key = key[1:] + (word,)

        words.append(word)

        # If word ends in punctuation, break out of the loop
        if word[-1] in punct:
            break

        word = choice(chains[key])

    return ' '.join(words)


# Get the filepath from the user through a command line prompt, ex:
# python markov.py green-eggs.txt

input_path = sys.argv[1:]

# This could also say something like:
#   input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, 2)

# Produce random text
random_text = make_text(chains)

print(random_text)
