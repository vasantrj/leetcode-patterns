"""
Problem: Longest Common Suffix Queries
LeetCode ID: 3093
Pattern: Trie / Strings
Difficulty: Hard
Time Complexity:
- Build Trie: O(total characters in wordsContainer)
- Query: O(total characters in wordsQuery)

Space Complexity: O(total characters)

Approach:
1. Reverse all words because:
   suffix matching becomes prefix matching.
2. Build a Trie using reversed container words.
3. At every Trie node store:
   - best_idx  -> index of best candidate word
   - best_len  -> shortest word length
4. "Best" means:
   - longest suffix match
   - if tie -> shorter word
   - if still tie -> smaller index
5. For each query:
   - traverse reversed query in Trie
   - stop when path breaks
   - answer = best_idx at deepest reachable node
"""

from typing import List

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.best_idx = -1
                self.best_len = float('inf')

        root = TrieNode()
        for idx, word in enumerate(wordsContainer):
            node = root
            if (
                len(word) < node.best_len or
                (
                    len(word) == node.best_len and
                    idx < node.best_idx
                )
            ):
                node.best_idx = idx
                node.best_len = len(word)

            for ch in reversed(word):
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                if (
                    len(word) < node.best_len or
                    (
                        len(word) == node.best_len and
                        idx < node.best_idx
                    )
                ):
                    node.best_idx = idx
                    node.best_len = len(word)

        result = []
        for query in wordsQuery:
            node = root
            for ch in reversed(query):
                if ch not in node.children:
                    break
                node = node.children[ch]
            result.append(node.best_idx)
        return result
    