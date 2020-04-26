from abc import ABC


class Person(ABC):
    __slots__ = "first_name", "last_name", "date_of_birth", "work_experience"

    def set_name(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self):
        return self.first_name, self.last_name
