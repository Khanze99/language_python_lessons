class Animal:
    def reply(self):
        self.speak()

    def speak(self):
        print('spam')


class Mammal(Animal):
    def speak(self):
        print('Mammal')


class Cat(Mammal):
    def speak(self):
        print("Meow meow motherfucka")


class Dog(Mammal):
    def speak(self):
        print("Gow gow mothefucka")


class Primate(Mammal):
    def speak(self):
        print("A A A A motherfucka")


class Hacker(Primate): pass
