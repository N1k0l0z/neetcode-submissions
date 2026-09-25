class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # If stack is empty, val is the current minimum
        # Otherwise, compare val against the previous minimum at the top of the stack
        current_min = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()  # O(1) time complexity

    def top(self) -> int:
        return self.stack[-1][0]  # O(1) time complexity

    def getMin(self) -> int:
        return self.stack[-1][1]  # O(1) time complexity