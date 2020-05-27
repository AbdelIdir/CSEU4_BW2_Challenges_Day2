class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.stack_helper = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)
        if not self.stack_helper:
            while self.stack:
                self.stack_helper.append(self.stack.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack_helper:
            while self.stack:
                self.stack_helper.append(self.stack.pop())
        return self.stack_helper.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.stack_helper:
            while self.stack:
                self.stack_helper.append(self.stack.pop())
        return self.stack_helper[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not (self.stack or self.stack_helper)

    def __str__(self):
        return str(self.stack)

stuff = MyQueue()

stuff.push(33)
stuff.push(34)
stuff.push(38)
stuff.push(37)


print("peek",stuff.peek())

print(stuff)


print(stuff.pop())



print(stuff.empty(),"<===== empty ,false or true")