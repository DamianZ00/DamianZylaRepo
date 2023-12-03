def check_value_in_list(lst, value):
    return value in lst

my_list = [1, 3, 5, 7, 9]

my_value = 5

result = check_value_in_list(my_list, my_value)

print(result)

my_value = 2

result = check_value_in_list(my_list, my_value)

print(result)