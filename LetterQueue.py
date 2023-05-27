"""
    In computer science, a queue is a particular kind of data type in
    which the entities in the collection are kept in order
    and the principal operations on the collection
    are the addition of entities to the rear terminal
    position (enqueue or push), and removal of entities
    from the front terminal position (dequeue or pop).
    This makes the queue a First-In-First-Out (FIFO) data structure.
    In a FIFO data structure, the first element added to the queue
    will be the first one to be removed.
    This is equivalent to the requirement that once a new element
    is added, all elements that were added before have to be removed
    before the new element can be removed.

    We will emulate the queue process with Python.
    You are given a sequence of commands:
    - "PUSH X" -- enqueue X , where X is a letter in uppercase.
    - "POP" -- dequeue the front position. if the queue is empty,
    then do nothing.

    The queue can only contain letters.

    You should process all commands and assemble letters which remain in the queue in one word from the front to the rear of the queue.

    Let's look at an example, here’s the sequence of commands:
    ["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]
    Command 	Queue 	Note
    PUSH A 	A 	Added "A" in the empty queue
    POP 		Removed "A"
    POP 		The queue is empty already
    PUSH Z 	Z
    PUSH D 	ZD
    PUSH O 	ZDO
    POP 	DO
    PUSH T 	DOT 	The result

    Input: A sequence of commands as a list of strings.

    Output: The queue remaining as a string.
"""

from typing import List


def letter_queue(commands: List[str]) -> str:
    res = []
    for command in commands:
        if "PUSH" in command:
            res.append(command[-1])
        elif command == "POP" and res:
            res.pop(0)
    return "".join(res)


def sequence(begin, end):
    if begin > end:
        return None
    elif begin == end:
        return begin
    return begin + sequence(begin + 1, end)


def smallestDev(num):
    if num < 1:
        return None
    count = 2
    half_num = num // 2
    while count <= half_num:
        if num % count == 0:
            return count
        count += 1
    return num


def isPrime(num):
    for i in range(1, num):
        if num % 2 == 0 or num % i == 0:
            return False
    return True


def triangleArea(h, b):
    return int(0.5 * h * b)


def addDigits(num):
    result = 0
    while num > 0:
        result += num % 10
        num = num // 10
    if result > 9:
        result = addDigits(result)

    return result


if __name__ == "__main__":
    print(sequence(1, 5))
    print(smallestDev(4))
    print(reverse("asdf"))
    print(isPrime(1))
    print(isPrime(21))
    print(isPrime(89))
    print(isPrime(29))

    print(isPrime(1451))
    print(triangleArea(5, 10))
    print(triangleArea(15, 12))
    print(addDigits(10))
    print(addDigits(19))
    print(addDigits(38))
