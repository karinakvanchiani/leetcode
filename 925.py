class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        def get_compact(string):
            compact = [[string[0], 1]]

            for i in range(1, len(string)):
                if compact[-1][0] == string[i]:
                    compact[-1][1] += 1
                else:
                    compact.append([string[i], 1])

            return compact

        compact_name = get_compact(name)
        compact_typed = get_compact(typed)

        if [letter[0] for letter in compact_name] != [letter[0] for letter in compact_typed]:
            return False

        for name_pair, typed_pair in zip(compact_name, compact_typed):
            if name_pair[0] == typed_pair[0] and name_pair[1] <= typed_pair[1]:
                continue
            else:
                return False

        return True