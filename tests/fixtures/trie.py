class Node():
    def __init__(self, value="", frequency=0.0):
        self.frequency = frequency
        self.value = value
        self.children = {}
        self.stop = False

    def __getitem__(self, key):
        if key in self.children:
            return self.children[key]
        return None
    
    def __setitem__(self, key, value):
        self.children[key] = value
    
    def __contains__(self, key):
        return key in self.children
    
    def __str__(self):
        return self.value
    
    def __iter__(self):
        for key in sorted(self.children.keys()):
            yield key

    def __delitem__(self, key):
        del self.children[key]

class Trie:
    def __init__(self):
        self.root = Node()

    def add_word(self, word, frequency):
        word = word.lower()
        current_node = self.root

        for letter in word:
            if letter not in current_node:
                current_node[letter] = Node(letter)
            current_node = current_node[letter]

        current_node.stop = True
        current_node.frequency = frequency


    @staticmethod
    def get_possible_matches(node, words_list, path):
        if node.stop:
            words_list.append((path + node.value, node.frequency))
        for letter in node.children:
            Trie.get_possible_matches(node.children[letter], words_list, path + node.value)

    def match_suffix(self, word):
        current_node = self.root
        for letter in word.lower():
            if letter in current_node:
                current_node = current_node[letter]
                # word += current_node.value
            else:
                return False

        possible_words = []
        self.get_possible_matches(current_node, possible_words, word[:-1])
        return possible_words



    def contains(self, word):
        current_node = self.root
        path = ""
        for letter in word.lower():
            if letter not in current_node:
                return False
            else:
                path += letter
                current_node = current_node[letter]
        if current_node.stop:
            return True
        return False

    def __contains__(self, key):
        return self.contains(key)

    @staticmethod
    def _print(node, path=""):
        if node.stop:
            print(path + node.value, node.frequency)
        for letter in node.children:
            Trie._print(node.children[letter], path + node.value)

    def print_content(self):
        for letter in self.root.children:
            self._print(self.root[letter])

if __name__ == "__main__":
    t = Trie()
    t.add_word("kaka")
    t.add_word("kakan")
    t.add_word("kakor")
    t.print_content()
    print("---------------")
    print(t.contains("kaka"))