class A():
    """Note that in this example class the actual x value is stored in the private variable __x.
    The attribute x is a PROPERTY OBJECT which provides interface to this private variable.
    Read this example thoroughly as well:
    https://www.programiz.com/python-programming/property
    """

    def __init__(self, x):
        # self.__x = x          # try this line in the debugger instead of the next one as well, step by step!
        self.x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x


if __name__ == "__main__":

    a = A(1)
    a.x = 2
    print(a.x)
