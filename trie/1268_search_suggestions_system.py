class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        prefix_tree = Trie()

        for product in products:
            prefix_tree.insert(product)

        return prefix_tree.suggest(searchWord)
            

class Trie:
    class Node:
        def __init__(self):
            self.children = {}
            self.is_terminal = False
            self.words = []

    def __init__(self):
        self.root = Trie.Node()

    def insert(self, word):
        node = self.root 
        for char in word:
            if char not in node.children:
                node.children[char] = Trie.Node()
            node = node.children[char]
            node.words.append(word)

        node.is_terminal = True
    
    def suggest(self, word):
        suggestions = []
        node = self.root
        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            suggestions.append(node.words[:3])
        for _ in range(len(word) - len(suggestions)):
            suggestions.append([])
        return suggestions