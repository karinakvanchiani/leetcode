def removeDuplicateLetters(s: str) -> str:
    def exist(indexes, taken_alphas, idx):
        for key, value in indexes.items():
            if key not in taken_alphas:
                if max(value) < idx:
                        return False
        return True

    indexes = {}
    order = sorted(set(s))
    num = len(order)

    for i, letter in enumerate(s):
        if letter not in indexes:
            indexes[letter] = []
        indexes[letter].append(i)

    taken_alphas = []
    last_idx = -1 # 2
    start = 0 # 
    # print(order)
    # for letter in order[start:]: # 'b'
    while order:
        letter = order[start]
        print('letter: ', letter)
        taken_alphas.append(letter) # ['a', 'b']
        if len(taken_alphas) == num:
            break
        letter_idxs = indexes[letter] # [2]
        for idx in letter_idxs: # 2
            if idx > last_idx and exist(indexes, taken_alphas, idx):
                last_idx = idx
                break
        if last_idx != idx:
            taken_alphas = taken_alphas[:-1]
            start = order.index(letter) + 1
        else:
            order.remove(letter)
            start = 0

        print(taken_alphas)
        continue

    if len(taken_alphas) < num:
        taken_alphas.append(order[-1])

    return ''.join(taken_alphas)

s = 'cdadabcc'
print(removeDuplicateLetters(s))