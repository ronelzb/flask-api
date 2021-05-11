from linked_list import LinkedList


class Queue(LinkedList):    
    def enqueue(self, data):
        super().add(data)

    def dequeue(self):
        return super().remove_first()

    def peek(self):
        return self.head

    def __str__(self):
        return super().__str__()


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(str(q))
    q.dequeue()
    print(str(q))
