class Person:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def print_person(self):
        return self.__name

    def print_person(self):
        return self.__address

    def print_person(self):
        return self.__phone


class Customer(Person):
    def __init__(self, name, address, phone, customer_no, mail):
        Person.__init__(self, customer_no, mail)

        self.__customer_no = customer_no
        self.__mail = mail
