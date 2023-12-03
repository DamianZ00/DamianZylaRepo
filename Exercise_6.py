def process_lists_and_return_result(list1, list2):
    # konkatenacja list
    combined_list = list1 + list2
    # zamienienie combined_list na typ danych set usuwa duplikaty,
    # następnie powrót do typu "list"
    unique_list = list(set(combined_list))
    result_list = [x ** 3 for x in unique_list]
    return result_list


list_a = [1, 2, 3]
list_b = [3, 4, 5]

result = process_lists_and_return_result(list_a, list_b)

print(result)
