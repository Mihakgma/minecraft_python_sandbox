class Singleton:
    __INSTANCE = None

    def __new__(cls, *args, **kwargs):
        if cls.__INSTANCE is None:
            cls.__INSTANCE = super().__new__(cls)
        return cls.__INSTANCE


class SomeClass(Singleton):
    pass

if __name__ == '__main__':
    obj1 = SomeClass()
    obj2 = SomeClass()
    print(obj1 == obj2)
