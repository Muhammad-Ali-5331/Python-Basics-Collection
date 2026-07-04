class Node:
    def __init__(self, val):
        self.value = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, value, nxt=None, prev=None):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def show(self):
        temp = self.head
        if temp:
            print("Current List: ", end=" ")
            while temp:
                print(temp.value, end=" -> ")
                temp = temp.next
            print("None")
        else:
            print("[!] Empty List")

    def append(self, value):
        new_node = Node(value)
        if self.head is not None:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length != 0:
            temp = self.tail
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
                temp.prev = None
            self.length -= 1

    def prepend(self, val):
        new_node = Node(val)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def popleft(self):
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        elif self.length > 1:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.head.prev = temp
            self.length -= 1
        elif self.length == 0:
            print("[!] Invalid Operation.....")

    def insert(self, value, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            self.prepend(value)
        elif index == self.length - 1:
            self.append(value)
        else:
            new_node = Node(value)
            temp = self.head
            for _ in range(index):
                temp = temp.next
            before = temp.prev
            after = temp.next
            new_node.prev = before
            before.next = new_node
            new_node.next = after
        self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            self.popleft()
        elif index == self.length - 1:
            self.pop()
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            before = temp.prev
            after = temp.next
            before.next = temp.next
            after.prev = before
            temp.next = temp.prev = None
        self.length -= 1


if __name__ == "__main__":
    my_list = DoublyLinkedList(7)
    my_list.append(8)
    my_list.append(9)
    my_list.prepend(4)
    # my_list.insert(5,1)
    print(my_list.length)
    # my_list.remove(3)
    my_list.show()
