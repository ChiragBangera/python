from itertools import combinations
import numpy as np


# pair_list = [
#     ("Susan", "spoon"),
#     ("Susan", "fork"),
#     ("Mark", "fork"),
#     ("Mark", "spoon"),
#     ("Mark", "plate"),
#     ("Lily", "plate"),
# ]


# def common_items(pair_list):
#     name_utensil = {}
#     for name, utensil in pair_list:
#         name_utensil.setdefault(name, []).append(utensil)

#     keys = list(name_utensil.keys())
#     pairs = combinations(sorted(keys), 2)
#     print(pairs)

#     res_list = []

#     for name1, name2 in pairs:
#         common_items_count = len(set(name_utensil[name1]) & set(name_utensil[name2]))
#         res_list.append((name1, name2, common_items_count))
#     return res_list


# print(common_items(pair_list))


# # for i in range(len(keys)):
# #     for j in range(i + 1, len(keys)):
# #         pairs.append((keys[i], keys[j]))

# # Create an array and traverse
# my_array = array("i", [1, 2, 3, 4, 5])
# for i in my_array:
#     print(i)

# # Access individual elements through indexes
# print(my_array[0])


# # Append any vaue to the array using append(method)

# my_array.append(6)
# print(my_array)

# # Insert value in an array using insert() method

# my_array.insert(0, 0)
# print(my_array)

# # Extend python array using extend() method
# my_array.extend([7, 8])
# print(my_array)

# # Add items from list into array using fromlist() method
# my_array.fromlist([9, 10, 11])
# print(my_array)

# # Remove any element using remove() method
# my_array.remove(5)
# print(my_array)

# # Remove last array element using pop() method
# my_array.pop(-1)
# print(my_array)

# # Fetch any element through its index using index() method
# print(my_array.index(10))

# # Reverse a ython array using reverse() method
# my_array.reverse()
# print(my_array)

# # Get array buffer information through buffer_info() method
# print(my_array.buffer_info())

# # Check for a number of occurrance of a number using count() method
# print(my_array.count(0))

# # Convert array to string using tostring() method
# print(my_array.tobytes())

# # Convert array to python list using tolits() method
# print(my_array.tolist())

# strtemp = my_array.tobytes()
# print(strtemp)
# print("---------------------Two Dimensional Array-----------------")

# twoDArray = np.array(
#     [[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]]
# )

# print(twoDArray)
# new2darray = np.insert(twoDArray, 0, [1, 2, 3, 4], axis=0)
# print(new2darray)
# print(np.mean(new2darray, axis=0))

# # Accesing an element of 2d array


# def access_elements(array, r_index, c_index):
#     if r_index >= len(array) or c_index >= len(array[0]):
#         return "index out of range"
#     return array[r_index][c_index]


# print(access_elements(new2darray, 4, 1))


# # treversing 2d array
# print([j for i in new2darray for j in i])


# # deleting 2d array has a time complexity of o(mn) and space complexity id o(mn)
# newdelarray = np.delete(twoDArray, 0, axis=0)
# print(newdelarray)


# # Python lists
# integers = [1, 2, 4, 3, 5]
# string_list = ["milk", "cheese", "bread"]
# mixed_list = ["Chirag", 1, 2, "Bangera"]
# nested_list = [1, 2, 3, 4, [1, 4, 6], ["test"]]

# print(integers + string_list)
# print(integers * 2)
# strg = "Chirag"
# b = list(strg)
# print(b)

# string_split = "Chirag Bangera is the greatest scientist"
# c = string_split.split()
# print(c)
# print(list(string_split))
# print(list(string_split).remove("C"))
# string_list[0] = "butter"
# print(string_list)


# lst = []
# while True:
#     if len(lst) == 3:
#         print(np.mean(lst))
#         break
#     print("Add number")
#     inp = input()
#     if inp.isnumeric():
#         lst.append(int(inp))
#     else:
#         print("only numbers allowed")
#         inp
def max_product(arr):
    # TODO
    prev_max = 0
    current_max = 0

    for i in arr:
        if i >= current_max:
            prev_max = current_max
            current_max = i
    return current_max * prev_max


arr = [1, 7, 3, 4, 9, 5, 9]
print(max_product(arr))
