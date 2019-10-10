class Father:

    def __init__(self):
        print("Father class constructor")


class Mother:

    def __init__(self):
        print("Mother class constructor")


class Son(Father, Mother):

    def __init__(self):
        print("Here start son")
        super(Father, self).__init__()
        print("Son class constructor")


papa = Father()
ma = Mother()
son = Son()
print(Son.mro())
