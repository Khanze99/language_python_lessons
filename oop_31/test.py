import tkinter

from listtree import ListTree


class MyButton(ListTree, tkinter.Button):
    pass


b = MyButton(text='spam')
print(b)