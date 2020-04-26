from base.worker import Worker
from abc import ABC, abstractmethod


class Programmer(Worker):
    __slots__: "technology_stack"

    @abstractmethod
    def who_is(self):
        pass

    def set_technology_stack(self, obj):
        self.technology_stack.append(obj)
    
    def get_technology_stack(self):
        return self.technology_stack