from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)


class Name(Field):
    ...


class Phone(Field):
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value: str):
        if len(new_value) != 10:
            raise ValueError("Phone number should be 10 digits long.")
        if not new_value.isdigit():
            raise ValueError("Phone number should only include digits.")
        self._value = new_value


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phone_numbers = []

    def add_phone(self, phone):
        self.phone_numbers.append(Phone(phone))

    def remove_phone(self, phone_to_remove):
        self.phone_numbers = list(
            filter(lambda phone: phone.value != phone_to_remove, self.phone_numbers))

    def edit_phone(self, old_phone, new_phone):
        search_for_phone = list(
            filter(lambda phone: phone.value == old_phone, self.phone_numbers))
        if search_for_phone:
            search_for_phone[0].value = new_phone
        else:
            raise ValueError('Phone number not found')

    def find_phone(self, phone_to_find):
        search_for_phone = list(
            filter(lambda phone: phone.value == phone_to_find, self.phone_numbers))
        if search_for_phone:
            return search_for_phone[0]

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {', '.join(p.value for p in self.phone_numbers)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name_value):
        return self.data.get(name_value)

    def delete(self, name):
        self.data.pop(name, None)
