from trie import Trie

class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, (list, tuple)):
            raise TypeError("strings must be a list or tuple of str")
        if not strings:
            return ""
        for s in strings:
            if not isinstance(s, str):
                raise TypeError("every element in strings must be str")

        super().__init__()
        for s in strings:
            self.put(s)

        node = self.root
        prefix_chars = []
        while len(node.children) == 1 and node.value is None:
            ch, node = next(iter(node.children.items()))
            prefix_chars.append(ch)

        return "".join(prefix_chars)

if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    print("All tests passed")