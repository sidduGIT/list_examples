class Stack:

    def __init__(self):
        self.stack=[]

    def is_empyt(self):
        if not self.stack:
            return True
        else:
            return False

    def push_stack(self,item):
        self.stack.append(item)

    def pop_stack(self):
        return self.stack.pop()

    def stack_size(self):
        return len(self.stack)

    def stack_peek(self):
        return self.stack[-1]


s=Stack()
print(s.is_empyt())
s.push_stack('dog')
s.push_stack(4)
s.push_stack('god')
s.push_stack(14.5)
s.push_stack('attu')
s.push_stack(141.5)

print(s.stack_size())
print(s.stack_peek())
print(s.pop_stack())
print(s.stack_size())
print(s.is_empyt())

