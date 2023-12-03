def is_even_number(number):
    return number % 2 == 0

input_number = 8
result = is_even_number(input_number)

if result:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
