from trie import TrieNode, Trie, IMDB_trie_factory

if __name__ == "__main__":
    import pickle
    import sys

    filename = sys.argv[1]

    sys.setrecursionlimit(5000)  # important, breaks otherwise
    t0 = pc()
    t = IMDB_trie_factory(filename)
    t1 = pc()
    print(t1 - t0)
    with open("IMBD_trie.pkl", "wb") as p:
        pickle.dump(t, p)
    print("saved")
    sys.setrecursionlimit(1000)