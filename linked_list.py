class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        new_node = ListNode(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

        return self.tail

    def add_first(self, data):
        new_node = ListNode(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        return self.head

    def to_list(self):
        return [x.data for x in self]

    def get_user_by_id(self, user_id):
        current = self.head
        user_id = int(user_id)

        while current and current.data["id"] is not user_id:
            current = current.next
        
        return current.data if current else None

    def remove_first(self):
        if not self.head:
            return None

        if self.head == self.tail:
            self.tail = None
        
        current = self.head
        self.head = self.head.next
        return current

    def __iter__(self):
        current = self.head

        while current:
            yield current
            current = current.next

    def __str__(self):
        return " -> ".join([str(x) for x in self])


if __name__ == "__main__":
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    ll.add_first(5)
    print(ll.to_list())
