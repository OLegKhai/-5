# test_structures.py

import pytest
from cat import ArrayStack, LinkedListStack, ArrayQueue, LinkedListQueue, Cat

def test_array_stack():
    stack = ArrayStack()
    assert stack.is_empty() == True
    stack.push(1)
    stack.push(2)
    assert stack.size() == 2
    assert stack.peek() == 2
    assert stack.pop() == 2
    assert stack.pop() == 1
    with pytest.raises(IndexError):
        stack.pop()

def test_linked_list_stack():
    stack = LinkedListStack()
    assert stack.is_empty() == True
    stack.push(1)
    stack.push(2)
    assert stack.size() == 2
    assert stack.peek() == 2
    assert stack.pop() == 2
    assert stack.pop() == 1
    with pytest.raises(IndexError):
        stack.pop()

def test_array_queue():
    queue = ArrayQueue()
    assert queue.is_empty() == True
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.size() == 2
    assert queue.front() == 1
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    with pytest.raises(IndexError):
        queue.dequeue()

def test_linked_list_queue():
    queue = LinkedListQueue()
    assert queue.is_empty() == True
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.size() == 2
    assert queue.get_front() == 1
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    with pytest.raises(IndexError):
        queue.dequeue()
