class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

print(MyClass.f)    # MyClass.f returns the function object created when def f(self) is executed! (So, this statement is OK.)
print()
print(MyClass.__doc__)
print()
x = MyClass()
print(x.i)
print(x.f())        # x.f is a method object, and MyClass.f (see above) is a function object - two DIFFERENT things
print()

xf = x.f
print(xf())
print(xf)
my_class_init = MyClass.__init__
print(my_class_init)
