from trie import Trie

class Homework(Trie):

    def has_prefix(self, prefix: str) -> bool:
        if not isinstance(prefix, str) or not prefix:
            raise TypeError("prefix must be a non-empty string")

        node = self.root
        for ch in prefix:
            node = node.children.get(ch)
            if node is None:
                return False
        return True

    def count_words_with_suffix(self, pattern: str) -> int:

        if not isinstance(pattern, str) or not pattern:
            raise TypeError("pattern must be a non-empty string")

        count = 0
        stack = [(self.root, "")]
        while stack:
            node, acc = stack.pop()
            if node.value is not None and acc.endswith(pattern):
                count += 1
            for ch, child in node.children.items():
                stack.append((child, acc + ch))
        return count


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Перевірка наявності префікса
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat

    print("All tests passed")
