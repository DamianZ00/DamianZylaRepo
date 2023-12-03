def create_greeting(name, surname):
    greeting = f"Cześć {name} {surname}!"
    return greeting

input_name = "Mariusz"
input_surname = "Pudzianowski"

result = create_greeting(input_name, input_surname)

print(result)
