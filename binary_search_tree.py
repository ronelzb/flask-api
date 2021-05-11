class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        
        if self.root is None:
            self.root = new_node
            return self.root
        
        current = self.root
        while current:
            if data["id"] == current.data["id"]:
                raise Exception("data already exist in the Binary Search Tree")
            if data["id"] < current.data["id"]:
                if current.left is None:
                    current.left = new_node
                    return current.left
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return current.right
                current = current.right
        
        return None

    def search(self, id):
        current = self.root

        while current:
            if id == current.data["id"]:
                return current.data
            elif id < current.data["id"]:
                current = current.left
            else:
                current = current.right

        return None

    def _get_nodes_preorder(self, node, level, output):
        if node is None:
            return output
        
        return ("\n" if level > 0 else "") + (" " * level * 2) + str(node) \
        + self._get_nodes_preorder(node.left, level + 1, output) \
        + self._get_nodes_preorder(node.right, level + 1, output)
        

    def __str__(self):
        if self.root is None:
            print("There is no nodes found in this Binary Search Tree")

        return self._get_nodes_preorder(self.root, 0, "")


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(2)
    bst.insert(3)
    bst.insert(1)
    bst.insert(7)
    bst.insert(6)
    bst.insert(8)
    print(str(bst))
