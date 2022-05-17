import enum


BugStatus = enum.Enum(value='BugStatus',  # название перечисления
                      # принимает строку, она разобьет на атрибуты(пробелом или запятой)
                      names=('fix_released fix_committed in_progress '
                             'wont_fix invalid incomplete new'),
                      )

BugStatusDict = enum.Enum(value='BuStatus',
                        names={'new': 7,
                               'incomplete': 2})

if __name__ == '__main__':

    print(f'Member: {BugStatus.new}')

    print('All members:')
    for status in BugStatusDict:
        print(f'{status.name:15} = {status.value}')