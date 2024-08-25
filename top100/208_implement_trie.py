class Node(object):
    def __init__(self):
        self.children = {}
        self.is_terminal = False

class Trie(object):

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for ch in word:
            if not node.children.get(ch):                
                node.children[ch] = Node()
            node = node.children[ch]            
        node.is_terminal = True


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        for ch in word:
            if not node.children.get(ch):
                return False
            node = node.children[ch]
        return node.is_terminal


    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for ch in prefix:
            if not node.children.get(ch):
                return False
            node = node.children[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)