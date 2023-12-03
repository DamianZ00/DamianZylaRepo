def display_even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number)

numbers_list = list(range(2, 21, 2))

display_even_numbers(numbers_list)
