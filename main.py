import pandas as pd
from trie_it_out import Trie
import pickle

def load_IMBD_trie(filename="IMBD_trie.pkl"):
    with open(filename, "rb") as f:
        return pickle.load(f)

def load_lookup(filename="IMBD_lookup.pkl"):
    with open(filename, "rb") as f:
