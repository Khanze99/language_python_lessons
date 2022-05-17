import asyncio


async def count_to_three():
    print("Веду счет. 1")
    await asyncio.sleep(0)
    print("Веду счет. 2")
    await asyncio.sleep(0)
    print("Веду счет. 3")
    await asyncio.sleep(0)


if __name__ == '__main__':
    coroutine_counter = count_to_three()
    print(coroutine_counter)

    coroutine_counter.send(None)
    coroutine_counter.send(None)
    coroutine_counter.send(None)
    coroutine_counter.send(None)