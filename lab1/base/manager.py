from .person import Person


class Manager(Person):
    __slots__ = "scope_of_work", "subordinates"

    def set_scope_of_work(self, scope):
        self.scope_of_work = scope

    def get_scope_of_work(self):
        return self.scope_of_work

    def set_subordinates(self, person):
        self.subordinates.append(person)

    def get_subordinates(self):
        return self.subordinates
