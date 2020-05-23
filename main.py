import pandas as pd
from trie_it_out import Trie, TrieNode
import pickle


def load_IMBD_trie(filename="pkl/IMBD_trie.pkl"):
    with open(filename, "rb") as f:
        return pickle.load(f)


def load_lookup(filename="pkl/IMBD_lookup.pkl"):
    with open(filename, "rb") as f:
        return pickle.load(f)


t = load_IMBD_trie()
l = load_lookup()

while True:
    value = input("Movie: ")
    suggestions = t.get_suggestions(value)
    movies = [l[s] for s in suggestions]
    print(movies)
