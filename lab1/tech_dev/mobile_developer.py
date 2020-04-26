from base.programmer import Programmer


class MobileDevepoler(Programmer):
    __slots__ = "platform"

    def who_is(self):
        print("I am mobile developer specified in " + self.get_platform())

    def set_platform(self, pl):
        self.platform = pl

    def get_platform(self):
        return self.platform
