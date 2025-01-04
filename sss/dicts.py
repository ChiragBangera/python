my_dict = {
    3:'three',
    2:'two',
    5:'five',
    9:'nine',
    7:'seven',
    1:'one'
}

print(3 in my_dict)
print('three' in my_dict.values())
print(all(my_dict))
print(sorted(my_dict))

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 

def count_word_frequency(words):
    # TODO
    res = {}
    for i in words:
        res[i] = res.get(i, 0) + 1
    return res

print(count_word_frequency(words))

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

set(list(dict1.keys()) + list(dict2.keys()))

def merge_sum(dict1, dict2):
    res = dict1.copy()

    for key, value in dict2.items():
        res[key] = res.get(key, 0) + value
    return res
print(merge_sum(dict1, dict2))  

my_dict = {'a': 5, 'b': 9, 'c': 2}

def max_value(dict):
    return max(my_dict, key=my_dict.get)

print(max_value(my_dict))