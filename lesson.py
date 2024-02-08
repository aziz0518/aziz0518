from datetime import datetime
import asyncio


async def task1():
    await asyncio.sleep(1)
    print("Task 1 completed")


async def task2():
    await asyncio.sleep(2)
    print("Task 2 completed")


async def task3():
    await asyncio.sleep(3)
    print("Task 3 completed")


async def task4():
    await asyncio.sleep(4)
    print("Task 4 completed")


async def task5():
    await asyncio.sleep(5)
    print("Task 5 completed")


async def task6():
    await asyncio.sleep(6)
    print("Task 6 completed")


async def task7():
    await asyncio.sleep(7)
    print("Task 7 completed")


async def task8():
    await asyncio.sleep(8)
    print("Task 8 completed")


async def main():
    await asyncio.gather(task1(), task2(), task3(), task4()), task5(), task6(), task7(), task8()


if __name__ == "__main__":
    print(datetime.now().time())
    asyncio.run(main())
    print(datetime.now().time())

# ----------------------------------------------------------------------------------------------
from datetime import datetime

import asyncio


async def task1():
    await asyncio.sleep(3)
    print("Task 1 completed")


async def task2():
    await asyncio.sleep(2)
    time = datetime.now().time()
    print(f"Task 2 completed {time}")


import json


async def task3():
    name = input("name = ")
    with open("test.json", "w") as file:
        json.dump({"name": name}, file, indent=6)
    await asyncio.sleep(5)
    time = datetime.now().time()
    print(f"Task 3 completed {time}")


async def task4():
    await asyncio.sleep(2)
    time = datetime.now().time()
    print(f"Task 4 completed {time}")


async def main():
    await asyncio.gather(task1(), task2(), task3(), task4())


if __name__ == "__main__":
    print(datetime.now().time())
    asyncio.run(main())
    print(datetime.now().time())
