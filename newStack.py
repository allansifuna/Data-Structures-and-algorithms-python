from node import Node


class Stack():
    def __init__(self):
        self.top = None

    def push(self, item):
        node = Node(item)
        curr = self.top
        if curr == None:
            self.top = node
        else:
            while curr != None:
                if curr.get_next() == None:
                    curr.next = node
                    return self
                curr = curr.get_next()
        return self

    def pop(self):
        curr = self.top
        prev = None
        while curr != None:
            if curr.get_next() == None:
                prev.next = None
                return curr.get_data()
            else:
                prev = curr
                curr = curr.get_next()

    def reverse(self):
        prev = None
        curr = self.top
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.top = prev
        return self

    def removeDuplicate(self):
        prev = self.top
        curr = self.top.next
        s = dict()
        while curr != None:
            if prev.get_data() not in s:
                s[prev.get_data()] = True
            if curr.get_data() in s:
                prev.set_next(curr.get_next())
                curr = curr.get_next()
                continue
            prev = curr
            curr = curr.get_next()
        return self

    def __str__(self):
        s = ""
        curr = self.top
        if curr == None:
            return s
        else:
            while curr != None:
                s += f"{curr.get_data()}->"
                curr = curr.get_next()
        return s[:-2]


stack = Stack()


def v(): return [stack.push(i) for i in range(10)]


v()
print(stack)
print()
print(stack.reverse())
print()
print(stack.removeDuplicate())
