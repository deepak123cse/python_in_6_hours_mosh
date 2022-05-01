class Person:
    def __init__(self, name):
        self.name = name


    def talk(self):
        print(f'Welcome to the program, {self.name}')


john = Person("John Smith")
john.talk()

ben = Person('Ben Ten')
ben.talk()