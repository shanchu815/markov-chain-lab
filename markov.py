"""Generate Markov text from text files."""

from random import choice
import sys

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    book_text = open(file_path)
    file_as_string = book_text.read()
    book_text.close()
    return file_as_string


def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    words = text_string.split()
    for i in range(len(words) - n):
        n_words = []
        for x in range(n):
            n_words.append(words[i+x])
        new_key = tuple(n_words)
        if new_key not in chains:
            chains[new_key] = [words[i+n]]
        else:
            chains[new_key].append(words[i+n])

    return chains


def make_text(chains, n):
    """Return text from chains."""

    #Getting first key in dictionary
    #res = list(test_dict.keys())[0]
    first_key = list(chains.keys())[0]
    #words = [first_key[0], first_key[1]]
    words = [first_key[i] for i in range(n)]
    # your code goes here
    #random.choice(sequence)
    # while True:
    new_word = choice(chains[first_key])
    new_key = tuple(list(first_key[1:]) + [new_word])
    words.append(new_word)
    while new_key in chains:
        new_word = choice(chains[new_key])
        new_key = tuple(list(new_key[1:]) + [new_word])
        words.append(new_word)
    #print(new_key)
    return ' '.join(words)


#input_path = 'green-eggs.txt'
#input_path = 'gettysburg.txt'
input_path = sys.argv[1]
n = int(sys.argv[2])
# n = 3
# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# # Get a Markov chain
chains = make_chains(input_text, n)

# # Produce random text
random_text = make_text(chains, n)

print(random_text)
