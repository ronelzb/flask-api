class HashData:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"{self.key}: {self.value}"

class HashNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * table_size
    
    def custom_hash(self, key):
        hash_value = 0
        
        for c in key:
            hash_value += ord(c)
            hash_value = (hash_value * ord(c)) % self.table_size
        
        return hash_value

    def add(self, key, value):
        hashed_key = self.custom_hash(key)

        if not self.hash_table[hashed_key]:
            self.hash_table[hashed_key] = HashNode(HashData(key, value))
        else:
            node = self.hash_table[hashed_key]
            while node.next:
                node = node.next
            
            node.next = HashNode(HashData(key, value))

    def get_value(self, key):
        hashed_key = self.custom_hash(key)
        node = self.hash_table[hashed_key]
        
        while node:
            if key == node.data.key:
                return node.data.value
            node = node.next

        return None

    def __str__(self):
        output = "{\n"
        
        for i, node in enumerate(self.hash_table):
            output += f"    [{i}] "
            if node:
                while node:
                    output += (
                        str(node.data.key) + ": " + str(node.data.value) + (" --> " if node.next else "")
                    )

                    node = node.next
            else:
                output += "None"
            output += "\n"

        output += "}"
        return output


if __name__ == "__main__":
    ht = HashTable(4)
    ht.add("hello", "world")
    ht.add("hi", "world")
    ht.add("rhino", "ant")
    print(str(ht))

    print(ht.get_value("hi"))
