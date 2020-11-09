

mixed = ['python', 'python2', 'python3', 'js', 'c++', 'lisp', 'ruby']
language = list(filter(lambda lang: 'python' in lang, mixed))

print(language)
