from typing import Tuple, List
import pandas as pd
from time import perf_counter as pc


class TrieNode:
    def __init__(self, char: str):
        self.char = char
        self.children = {}
        self.word_finished = False
        self.counter = 1
        self.ids = set()  # store movie ids

    def __repr__(self):
        return f"{self.char}"


class Trie:
    def __init__(self):
        self.root = TrieNode("ROOT")

    def add_title(self, title: str, id: str):
        """
        Add the word to the given trie (root)
        """
        node = self.root
        for char in title:
            if char in node.children:
                temp = node.children[char]
                temp.counter += 1
                node = temp
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.word_finished = True
        node.ids.add(id)

    def search(self, prefix) -> bool:
        """
        Full Match search!
        """
        node = self.root
        found = True
        for char in prefix:
            if not node.children.get(char):
                found = False
                break
            node = node.children.get(char)

        return node and node.word_finished and found

    def suggestions(self, node: TrieNode, prefix: str, result: List):
        """
        recursion?
        """
        if len(result) >= 10:
            return result
        if node.word_finished:
            result.extend(node.ids)

        for c, n in node.children.items():
            self.suggestions(n, prefix + c, result)

    def get_suggestions(self, prefix):
        node = self.root
        not_found = False
        temp = ""

        for c in prefix:
            if not node.children.get(c):
                not_found = True
                break
            temp += c
            node = node.children.get(c)

        if not_found:
            return 0

        result_set = []
        self.suggestions(node, temp, result_set)
        return result_set


def IMDB_trie_factory(filename):
    """
    Create and populate a trie with IMBD data
    return the trie object
    """
    imdb_trie = Trie()
    df = pd.read_csv(filename, sep="\t", usecols=["tconst", "primaryTitle"])
    for _, row in df.iterrows():
        imdb_trie.add_title(row["primaryTitle"], row["tconst"])
    return imdb_trie


if __name__ == "__main__":
    import pickle
    import sys

    sys.setrecursionlimit(5000)  # important, breaks otherwise
    t0 = pc()
    t = IMDB_trie_factory("movies_only.tsv")
    t1 = pc()
    print(t1 - t0)
    with open("IMBD_trie.pkl", "wb") as p:
        pickle.dump(t, p)
    print("saved")
    sys.setrecursionlimit(1000)
