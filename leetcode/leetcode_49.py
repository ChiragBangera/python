strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


def group_anagrams(anagrams):

    data = {}

    for s in anagrams:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1

        data.setdefault(tuple(count), [])
        data[tuple(count)].append(s)

    return data
