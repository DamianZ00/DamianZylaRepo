def display_every_second_element(numbers):
    for i in range(0, len(numbers), 2):
        print(numbers[i])

numbers_list = list(range(1, 11))

display_every_second_element(numbers_list)
