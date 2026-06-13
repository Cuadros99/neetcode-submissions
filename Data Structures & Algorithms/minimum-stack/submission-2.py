class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        minor = min(val, self.min_value[-1] if self.min_value else val) 
        self.min_value.append(minor)

    def pop(self) -> None:
        val = self.stack.pop()
        self.min_value.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_value[-1]
