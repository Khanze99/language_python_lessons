

class Animal2:  # solves 2 problems, not principle single responsibility
    def __init__(self, name: str):
        ...

    def get_animal_name(self):
        ...

    def save_animal(self, animal):
        ...


class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_animal_name(self):
        return self.name


class AnimalDB:
    def get_animal(self, a: Animal):
        # get from db
        return a

    def save_animal(self, a: Animal):
        # save to db
        return a
