import types
from collections import namedtuple

db = namedtuple('db', 'data')
db.data = [1, 2, 3]


@types.coroutine
def read_data(db):
    while True:
        yield db.data


async def process_data(db):
    while True:
        data = await read_data(db)
        print(data)


if __name__ == '__main__':
    pd = process_data(db)
    process_data()
