def add_subtract_numbers(number_1, number_2, *args):
    print(args)
    return number_1 + number_2, number_1 - number_2


start_number = 1
add_number = 4

input_values = {"number_1": start_number, "number_2": add_number}

print(input_values)

add, sub = add_subtract_numbers(1, 2, 3, 4, **input_values)
print(add, sub)


# %%
outside_variable = 5


def test_function(x):

    global outside_variable
    outside_variable = 50
    y = x + outside_variable
    return y


test_function(35)

# %%
