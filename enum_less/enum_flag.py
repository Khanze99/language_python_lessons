from enum import Flag


def show_chores(chores, day):
    for chore, days in chores.items():
        if day in days:
            print(chore)


class WeekDay(Flag):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 4
    THURSDAY = 8
    FRIDAY = 16
    SATURDAY = 32
    SUNDAY = 64


first_week_day = WeekDay.MONDAY
print(first_week_day)

weekend = WeekDay.SATURDAY | WeekDay.SUNDAY
print(repr(weekend))


chores_for_ethan = {
    'feed the cat': WeekDay.MONDAY | WeekDay.WEDNESDAY | WeekDay.FRIDAY,
    'do the dishes': WeekDay.TUESDAY | WeekDay.THURSDAY,
    'answer SO questions': WeekDay.SATURDAY,
    }

show_chores(chores_for_ethan, WeekDay.SATURDAY)

