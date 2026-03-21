from collections import defaultdict

def group_anagrams(strs):
    mp = defaultdict(list)

    for str in strs:
        str_sorted = "".join(sorted(str))
        mp[str_sorted].append(str)

    return list(mp.values())
