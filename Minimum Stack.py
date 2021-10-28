class MinimumStack:
    def __init__(self):
        self.data = []
        self.minimum = [float('inf')]

    def append(self, val):
        if self.minimum[-1] > val:
            self.minimum.append(val)
        self.data.append(val)
        

    def peek(self):
        if self.data:
            return self.data[-1]
        return None
    def min(self):
        return self.minimum[-1]

    def pop(self):
        pop_val = self.data.pop()
        if pop_val == self.minimum[-1]:
            self.minimum.pop()
        return pop_val