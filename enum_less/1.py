from enum import Enum
from datetime import date


class WeekDay(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    @classmethod
    def from_date(cls, date):
        return cls(date.isoweekday())


print(WeekDay.MONDAY)
print(type(WeekDay.MONDAY))
print(repr(WeekDay.MONDAY))
print(list(WeekDay))

print(isinstance(WeekDay.MONDAY, WeekDay))

print(WeekDay.SUNDAY.name)
print(WeekDay.SUNDAY.value)

print(repr(WeekDay.from_date(date.today())))


print(WeekDay(1))
print(WeekDay(7))

print(WeekDay['MONDAY'])
