from typing import Tuple, List

class TrieNode:
    def __init__(self, char: str):
        self.char = char
        self.children = {}
        self.word_finished = False
        self.counter = 1
        self.ids = set() # store movie ids

    def __repr__(self):
        return f"{self.char}"


def add_titles(root: TrieNode, title: str, id: str):
    """
    Add the word to the given trie (root)
    """
    node = root
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


def trie_factory(words: List[str]):
    """
    create and populate a trie, return the root node
    """
    root = TrieNode("TRIE START")
    for word in words:
        add_titles(root, word, 1)
    return root