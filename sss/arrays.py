from itertools import combinations


pair_list = [
    ("Susan", "spoon"),
    ("Susan", "fork"),
    ("Mark", "fork"),
    ("Mark", "spoon"),
    ("Mark", "plate"),
    ("Lily", "plate"),
]


def common_items(pair_list):
    name_utensil = {}
    for name, utensil in pair_list:
        name_utensil.setdefault(name, []).append(utensil)

    keys = list(name_utensil.keys())
    pairs = combinations(sorted(keys), 2)
    print(pairs)

    res_list = []

    for name1, name2 in pairs:
        common_items_count = len(set(name_utensil[name1]) & set(name_utensil[name2]))
        res_list.append((name1, name2, common_items_count))
    return res_list


print(common_items(pair_list))


# for i in range(len(keys)):
#     for j in range(i + 1, len(keys)):
#         pairs.append((keys[i], keys[j]))
