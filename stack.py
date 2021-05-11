from linked_list import LinkedList


class Stack(LinkedList):    
    def push(self, data):
        super().add_first(data)

    def pop(self):
        return super().remove_first()

    def peek(self):
        return self.head

    def __str__(self):
        return super().__str__()


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(str(s))
    s.pop()
    print(str(s))
