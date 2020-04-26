from base.programmer import Programmer


class WebDeveloper(Programmer):
    __slots__ = "platform"

    def set_platform(self, pl):
        self.platform = pl

    def get_platform(self):
        return self.platform

    def who_is(self):
        print("I am web developer specified in " + self.get_platform)
