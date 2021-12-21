"""
Перегрузка операций.
Напишите класс по имени MyList, который скрывает ("помещает внутрь себя")
список Python: он должен перегружать большинство списковых операций, влючая +, индексирование,
итерацию, нарезаниеЮ а так же списковые методы, такие как append и sort.
Перечень всех возможных методов для поддержки ищите в справочном руководстве
по Python или в другой документации.
К тому же предоставьте для своего класса конструктор, который принимает существующий список (или экземпляр MyList)
и копирует его компоненты в атрибут экземпляра. Поэкспериментируйте с классом интерактивно.

1) Почему здесь важно копирование начального значения? Так как мы имеем дело с изменяемым объектом

2) Можете ли вы использовать пустой срез (например, start[:]) для копирования начаьлного
значения, если он является экземпляром MyList? Да, так как есть __getitem__

3) Имеется ли общий способ для маршрутизации внутреннему списку обращений к списковым методам?
Да, так как объект в атрибуте экземпляра поддерживает списковые методы

4) Можете ли вы сложить экземпляр MyList и нормальный список? Список и экземпляр MyList?
Да, перенаправить в __add__ или переписать __radd__

5) Какой тип должны возвращать операции вроде + и нарезания? Как насчет операций индексирования?
+ ничего не должен по сути позвращать, мы меняем обхект на месте, нарезание вернет список

6) Если вы работаете с относительно свежим выпуском Python, то можете реализовать класс оболочки
такого рода за счет внедрения реального списка внутрь автономного класса или путем расширения
встроенного спискового типа посредством подкласса. Что легче и почему?

легче реализовать подкласс, тк нужные методы есть в родителе
"""


class MyList:
    def __init__(self, data):
        self.data = data[:]

    def __add__(self, other):
        self.data.extend(other)

    def __radd__(self, other):
        self.__add__(other)

    def __getitem__(self, item):
        return self.data[item]

    def __iter__(self):  # iter --> next
        for i in self.data:
            yield i

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.data}"

    def __len__(self, other):
        return len(self.data)

    def __getattr__(self, item):
        return getattr(self.data, item)


class MyListSub(MyList):

    calls = 0

    def __init__(self, data):
        MyList.__init__(self, data)
        self.count = 0

    def __add__(self, other):
        self.count += 1
        MyListSub.calls += 1
        print(f"{self.data} + {other}. Count call + {self.count}")
        super().__add__(other)

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.data}"

    @property
    def stats(self):
        return f"Instances call {self.__class__.__name__}: {MyListSub.calls}, Instance {self.__class__} call add: {self.count}"

