from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, phone):
        if not phone.isdigit() or len(phone) != 10:
            raise ValueError("Phone number must be exactly 10 digits.")
        super().__init__(phone)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, number):
        self.phones.append(Phone(number))

    def remove_phone(self, number):
        self.phones = [phone for phone in self.phones if phone.value != number]

    def edit_phone(self, old_number, new_number):
        for phone in self.phones:
            if phone.value == old_number:
                phone.value = new_number

    def find_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __str__(self):
        contacts_str = ', '.join(f"{phones}" for name, phones in self.data.items())
        return f"Contacts: {contacts_str}"

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name_look_for):
        return self.data.get(name_look_for)

    def delete(self, name_to_delete):
        if name_to_delete in self.data:
            del self.data[name_to_delete]


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
try:
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    book.add_record(john_record)
except ValueError as e:
    print(e)

# Створення та додавання нового запису для Jane
try:
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)
except ValueError as e:
    print(e)

# Виведення всіх записів у книзі
print(book)  # Виведення: Contacts: Contact name: John, phones: 1234567890; 5555555555, Contact name: Jane, phones: 9876543210

# Знаходження та редагування телефону для John
john = book.find("John")
if john:
    try:
        john.edit_phone("1234567890", "1112223333")
        print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555
    except ValueError as e:
        print(e)

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555") if john else None
if found_phone:
    print(f"{john.name.value}: {found_phone.value}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")
print(book)  # Виведення: Contacts: Contact name: John, phones: 1112223333; 5555555555