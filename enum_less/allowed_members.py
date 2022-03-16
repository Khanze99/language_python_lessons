from enum import Enum


class Mood(Enum):
    FUNKY = 1
    HAPPY = 3

    def describe(self):
        return self.name, self.value

    def __str__(self):
        return f'my custom str! {self.value}'

    @classmethod
    def favorite_mood(cls):
        return cls.HAPPY


print(repr(Mood.favorite_mood()))
print(Mood.HAPPY.describe())
print(str(Mood.FUNKY))
