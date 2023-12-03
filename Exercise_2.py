class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library: {self.city}, {self.street}, {self.zip_code},
        {self.open_hours}, {self.phone}"


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date,
                 city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name},
        {self.hire_date}, {self.birth_date}, {self.city},
        {self.street}, {self.zip_code}, {self.phone}"


class Book:
    def __init__(self, library, publication_date, author_name,
                 author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book: {self.author_name} {self.author_surname},
        {self.publication_date}, {self.number_of_pages},
        {str(self.library)}"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_info = "\n".join([str(book) for book in self.books])
        return f"Order: {str(self.employee)}, {str(self.student)},
        Books: \n{books_info}, {self.order_date}"


library1 = Library("Katowice", "ul. Sandomierska 15", "40-216",
                   "9:00 - 17:00", "123-456-789")
library2 = Library("Wadowice", "ul. Zamkowa 16", "22-222",
                   "10:00 - 18:00", "987-654-321")

employee1 = Employee("Adam", "Małysz", "2022-01-01", "1990-05-15",
                     "Katowice", "ul. Katowicka",
                     "40-215", "111-222-333")
employee2 = Employee("Kamil", "Stoch", "2022-02-01", "1985-08-20",
                     "Zakopane", "ul. Adama Małsza 39",
                     "66-212", "444-555-666")

book1 = Book(library1, "1599-01-01", "William", "Shakespeare", 200)
book2 = Book(library1, "1603-02-02", "William", "Shakespeare", 250)
book3 = Book(library2, "1813-01-28", "Wisława", "Szymborksa", 300)
book4 = Book(library2, "1817-07-18", "Władysław", "Rejmont", 180)
book5 = Book(library2, "1847-06-09", "Dawid", "Kubacki", 220)

order1 = Order(employee1, "Damian Żyła", [book1, book2], "2023-06-01")
order2 = Order(employee2, "Żamian Dyła", [book3, book4, book5], "2023-06-02")

print(order1)
print(order2)
