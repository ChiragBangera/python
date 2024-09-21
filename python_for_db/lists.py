example_list = [1, 2, 34, 5, 6, 7]

print(len(example_list))

example_list.append('10000')

print(example_list)

example_list_two = example_list[:4]

combined_list = example_list + example_list_two

print(combined_list)

our_first_dictionary = {'key': 'value', 'key_2': 'value_2', 2: 4, 4: 9, 'Chirag': 'Bangera'}

del our_first_dictionary['key']
print(our_first_dictionary.values())
print(our_first_dictionary.get('Chirag', 'Hunter'))

our_first_dictionary.setdefault('Amazon', 0)
print(our_first_dictionary)