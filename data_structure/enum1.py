import enum


class BugStatus(enum.Enum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1


class BugStatusInt(enum.IntEnum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1


class BugStatusAliases(enum.IntEnum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

    # тк by_design и closed являются синонимами для других элементов,
    # то они не появляются как элементы в циклах. Истинным считается название,
    # указанное первым пи объявлении
    by_design = 4
    closed = 1


@enum.unique
class BugStatusAliasesUnique(enum.IntEnum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1


if __name__ == '__main__':
    # атрибуты конвертируются в экземпляры при парсинге.
    # где каждый атрибут имеет параметр имени и значения
    print(f'\nMember name: {BugStatus.wont_fix.name}')
    print(f'Member value: {BugStatus.wont_fix.value}')

    # Итерирование

    for status in BugStatus:
        print(f'{status.name:15} = {status.value}')

    # Сравнение перечислений
    actual_state = BugStatus.wont_fix
    desired_state = BugStatus.fix_released

    print('Equality:',
          actual_state == desired_state,
          actual_state == BugStatus.wont_fix
          )

    print('Identity',
          actual_state is desired_state,
          actual_state is BugStatus.wont_fix
          )
    print('Ordered by value:')
    try:
        print('\n'.join(' ' + s.name for s in sorted(BugStatus)))
    except TypeError as err:
        print(f'Cannot sort: {err}')

    # Для возможности сравнения можно использовать IntEnum
    print('Ordered by value:')
    print('\n'.join(' ' + s.name for s in sorted(BugStatusInt)))

    print('\n')
    for status in BugStatusAliases:
        print(f'{status.name:15} = {status.value}')

    print(f'\nSame: by_design is wont_fix:',
          BugStatusAliases.by_design is BugStatusAliases.wont_fix)

    print(f'\nSame: closed is fix_released:',
          BugStatusAliases.closed is BugStatusAliases.fix_released)
