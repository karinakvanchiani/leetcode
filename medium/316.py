class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        def exist(indexes, idx):
            for value in indexes.values():
                if max(value) < idx:
                    return False
            return True

        indexes = {}

        for i, letter in enumerate(s):
            if letter not in indexes:
                indexes[letter] = []
            indexes[letter].append(i)

        s = sorted(set(s))
        num = len(s)

        taken_alphas = []
        last_idx = -1
        start = 0
        while s:
            letter = s[start]
            if len(taken_alphas) + 1 == num:
                break
            letter_idxs = indexes[letter]
            for idx in letter_idxs:
                if idx > last_idx and exist(indexes, idx):
                    last_idx = idx
                    taken_alphas.append(letter)
                    s.remove(letter)
                    del indexes[letter]
                    start = 0
                    break

            if last_idx != idx:
                start = s.index(letter) + 1
            continue

        taken_alphas.append(s[-1])
        return ''.join(taken_alphas)
