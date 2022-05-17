import enum


class BugStatus(enum.Enum):

    new = (7, ['incomplete', 'invalid', 'wont_fix', 'in_progress'])
    incomplete = (6, ['new', 'wont_fix'])
    invalid = (5, ['new'])
    wont_fix = (4, ['new'])
    in_progress = (3, ['new', 'fix_committed'])
    fix_committed = (2, ['in_progress', 'fix_released'])
    fix_released = (1, ['new'])

    def __init__(self, num, transitions):
        self.num = num
        self.transitions = transitions

    def can_transitions(self, new_state):
        return new_state.name in self.transitions


if __name__ == '__main__':

    print('Name:', BugStatus.in_progress)
    print('Value:', BugStatus.in_progress.value)
    print('Custom Attribute:', BugStatus.in_progress.transitions)
    print('Custom Attribute:', BugStatus.in_progress.num)
    print('Using attribute:', BugStatus.in_progress.can_transitions(BugStatus.invalid))
