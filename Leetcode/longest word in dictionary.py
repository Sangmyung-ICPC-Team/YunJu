class Solution:
    def longestWord(self, words: List[str]) -> str:
        result = ''
        words.sort()

        hash = set([''])

        for word in words:
            if word[:-1] in hash:
                hash.add(word)

                if len(word) > len(result):
                    result = word
        return result