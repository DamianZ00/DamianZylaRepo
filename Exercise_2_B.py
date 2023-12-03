#Wersja z pętlą for
def multiply_by_two_1(numbers):
    for number in numbers:
        print(number * 2)


#Wersja z listą składaną
def multiply_by_two_2(numbers):
    print([i*2 for i in numbers])


ws_numbers = [1,2,3,4,5]

multiply_by_two_1(ws_numbers)
multiply_by_two_2(ws_numbers)