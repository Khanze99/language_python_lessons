test_cases = ['([](){([])})', '()[]}', '{{[()]]']

brackets_dict = {'(': 1, ')': 2, '[': 3, ']': 4, '{': 5, '}': 6}
# verification_object = str(input())


def verification(verification_object):
    stack = []

    for symbol in enumerate(verification_object, 1):
        last_element = None if len(stack) == 0 else stack[len(stack) - 1]

        if symbol[1] in brackets_dict.keys():
            if last_element:
                if set(symbol[1]) & {'[', '(', '{'}:
                    stack.append(symbol)
                    continue

                if set(symbol[1]) & {']', ')', '}'}:
                    if set(last_element[1]) & {'[', '(', '{'}:
                        if brackets_dict[last_element[1]] + 1 == brackets_dict[symbol[1]]:
                            stack.pop()
                            continue

            if symbol[1] in {']', ')', '}'}:
                return symbol[0]

            stack.append(symbol)
        else:
            continue

    if stack:
        return stack.pop()[0]
    else:
        return 'Success'


assert verification("([](){([])})") == 'Success'
assert verification("()[]}") == 5
assert verification("{{[()]]") == 7
assert verification("{{{[][][]") == 3
assert verification("{*{{}") == 3
assert verification("[[*") == 2
assert verification("{*}") == 'Success'
assert verification("{{") == 2
assert verification("{}") == 'Success'
assert verification("") == 'Success'
assert verification("}") == 1
assert verification("*{}") == 'Success'
assert verification("{{{**[][][]") == 3
assert verification('()({}') == 3
assert verification('{{[()]}') == 1
assert verification('[]') == 'Success'
assert verification('{}[]') == 'Success'
assert verification('[()]') == 'Success'
assert verification('(())') == 'Success'
assert verification('{[]}()') == 'Success'
assert verification('([](){([])})') == 'Success'
assert verification('foo(bar);') == 'Success'
assert verification('{') == 1
assert verification('{[}') == 3
assert verification('()[]}') == 5
assert verification('{{[()]]') == 7
assert verification('foo(bar[i);') == 10
assert verification('[]([]') == 3
assert verification('([{') == 3
assert verification('{{{[][][]') == 3
assert verification(']]]') == 1
assert verification('dasdsadsadas]]]') == 13



# слишком много кода и проверок, возможно можно сделать более удобнее
