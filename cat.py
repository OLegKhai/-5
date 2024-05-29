from typing import List, Union, Iterable
from abstractstructure import AbstractCatArray

class Cat:
    def __init__(self, name: str, breed: str, color: str, age: Union[int, float], weight: Union[int, float], category: str) -> None:
        self.name = name
        self.breed = breed
        self.color = color
        if isinstance(age, (int, float)):
            self.age = round(float(age), 1)
        else:
            raise ValueError("Age must be a number")
        if isinstance(weight, (int, float)):
            self.weight = round(float(weight), 1)
        else:
            raise ValueError("Weight must be a number")
        self.category = category

    def __repr__(self) -> str:
        return f"Cat({self.name}, {self.breed}, {self.color}, {self.age}, {self.weight}, {self.category})"
    
    def __eq__(self, other):
        if isinstance(other, Cat):
            return (
                self.name == other.name and
                self.breed == other.breed and
                self.color == other.color and
                self.age == other.age and
                self.weight == other.weight and
                self.category == other.category
            )
        return False

class CatArray(AbstractCatArray):
    def __init__(self, initial_data: List[Cat] = None) -> None:
        if initial_data is None:
            self.data = []
        else:
            self.data = list(initial_data)

    def __len__(self) -> int:
        return len(self.data)

    def __repr__(self) -> str:
        return repr(self.data)

    def __getitem__(self, index: int) -> Cat:
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of range")
        return self.data[index]

    def __setitem__(self, index: int, value: Cat) -> None:
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of range")
        self.data[index] = value

    def append(self, value: Cat) -> None:
        self.data.append(value)

    def insert(self, index: int, value: Cat) -> None:
        if index < 0 or index > len(self.data):
            raise IndexError("Index out of range")
        self.data.insert(index, value)

    def index(self, value: Cat, start: int = 0, stop: int = None) -> int:
        if stop is None:
            stop = len(self.data)
        for i in range(start, stop):
            if self.data[i] == value:
                return i
        raise ValueError(f"{value} is not in list")

    def remove(self, value: Cat) -> None:
        for i in range(len(self.data)):
            if self.data[i] == value:
                del self.data[i]
                return
        raise ValueError(f"{value} not found in list")
    
    def clear(self) -> None:
        self.data = []

    def copy(self) -> list:
        return self.data.copy()

    def __iter__(self) -> Iterable:
        return iter(self.data)

    def __next__(self) -> Cat:
        raise NotImplementedError("Custom iterator not implemented for CatArray")

    def __delitem__(self, key) -> None:
        del self.data[key]

    def extend(self, values: Iterable[Cat]) -> None:
        self.data.extend(values)

    def pop(self, index: int = -1) -> Cat:
        return self.data.pop(index)

    def reverse(self) -> None:
        self.data.reverse()

    def count(self, value: Cat) -> int:
        return self.data.count(value)
    
class ArrayStack:
    def __init__(self):
        self.array = []

    def is_empty(self):
        return len(self.array) == 0

    def push(self, item):
        self.array.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.array.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.array[-1]

    def size(self):
        return len(self.array)

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        item = self.head.data
        self.head = self.head.next
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.head.data

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    
class ArrayQueue:
    def __init__(self):
        self.array = []

    def is_empty(self):
        return len(self.array) == 0

    def enqueue(self, item):
        self.array.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.array.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self.array[0]

    def size(self):
        return len(self.array)

class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
        if self.front is None:
            self.front = self.rear

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return item

    def get_front(self):
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self.front.data

    def size(self):
        current = self.front
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def __iter__(self):
        current = self.front
        while current:
            yield current
            current = current.next




def demo_stack():
    print("Демонстрация работы стека с объектами Cat")

    stack = ArrayStack()
    cat1 = Cat("Барсик", "Персидська", "білий", 0.3, 1.5, "довгошерстий")
    cat2 = Cat("Мурзик", "Сіамська", "сірий", 2, 4.5, "короткошерстий")
    cat3 = Cat("Василий", "Мейн-кун", "чёрный", 1.5, 5.2, "довгошерстий")

    stack.push(cat1)
    stack.push(cat2)
    stack.push(cat3)

    print("Стек после добавления трёх котов:", stack.array)

    popped_cat = stack.pop()
    print("Извлечённый кот:", popped_cat)
    print("Стек после извлечения:", stack.array)

    print("Верхний элемент стека:", stack.peek())
    print("Размер стека:", stack.size())

def demo_queue():
    print("Демонстрация работы очереди с объектами Cat")

    queue = LinkedListQueue()
    cat1 = Cat("Барсик", "Персидська", "білий", 0.3, 1.5, "довгошерстий")
    cat2 = Cat("Мурзик", "Сіамська", "сірий", 2, 4.5, "короткошерстий")
    cat3 = Cat("Василий", "Мейн-кун", "чёрный", 1.5, 5.2, "довгошерстий")

    queue.enqueue(cat1)
    queue.enqueue(cat2)
    queue.enqueue(cat3)

    print("Очередь после добавления трёх котов:", [node.data for node in iter(queue)])

    dequeued_cat = queue.dequeue()
    print("Извлечённый кот:", dequeued_cat)
    print("Очередь после извлечения:", [node.data for node in iter(queue)])

    print("Первый элемент очереди:", queue.get_front())
    print("Размер очереди:", queue.size())

if __name__ == "__main__":
    demo_stack()
    demo_queue()
