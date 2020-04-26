from .person import Person


class Worker(Person):
    __slots__ = "is_intern", "department", "chief", "status"

    def set_is_intern(self, answer):
        self.is_intern = answer

    def get_is_intern(self):
        return self.is_intern

    def set_department(self, d):
        self.department = d

    def get_department(self):
        return self.department

    def set_chief(self, c_name):
        self.chief = c_name

    def get_chief(self):
        return self.chief

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status
