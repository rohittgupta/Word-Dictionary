class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def starts_with(self, prefix: str) -> list:
        res, node = [], self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]

        def dfs(curr, path):
            if curr.is_end:
                res.append(path)
            for ch, child in curr.children.items():
                dfs(child, path + ch)
        dfs(node, prefix)
        return res

    def all_words(self) -> list:
        return self.starts_with("")
