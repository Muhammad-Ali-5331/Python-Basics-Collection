class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)  # Creates Node with value and next as None
        self.head = new_node  # Pointing to first element
        self.tail = new_node  # pointing to last element
        self.length = 1

    def print_list(self):  # Prints the list if it doesn't point to None
        if self.head:
            print("[+] Current Linked List: ", end=" ")
            temp = self.head
            while temp:
                print(f"{temp.value}", end="->")
                temp = temp.next
            print("None")
        else:
            print("[!] Linked List is Empty....")

    def append(self,
               value):  # Adds a node to the end of linked list. If list is empty it points both head and tail to newly created node.
        new_node = Node(value)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head and self.tail:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.tail is None:
            print("[!] Couldn't pop element because both (head,tail) points to None")
        elif self.tail == self.head:
            print(f"[+] Both (head,tail) were pointing to {self.head.value}, so changed their pointing to None.")
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            temp = self.head
            current = temp
            while temp.next:
                current = temp
                temp = temp.next
            print(f"[+] Dropping {temp.value}...")
            self.tail = current
            self.tail.next = None
            self.length -= 1
            ''' Approach #2: else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            print(f"[+] Dropping {temp.next.value}...")
            self.tail = temp
            self.tail.next = None
            print(f"[+] New tail: {self.tail.value}")
            self.print_list()
'''

    def popFirst(self):
        if self.head:
            print(f"[+] Dropping {self.head.value}...")
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.length -= 1
        else:
            print("[!] Could not pop first element cause head points to None")

    def getByIndex(self, index):
        if index < 0 or index > self.length - 1:
            print(f"[!] Invalid Index (Out of range Index): {index}")
        else:
            temp = self.head
            i = 0
            while i < index:
                temp = temp.next
                i += 1
            print(f"[+] Value at index {index} of LinkedList is: {temp.value}")
            return temp

    def getByValue(self, value):
        temp = self.head
        for _ in range(self.length):
            if temp.value == value:
                print(f"[+] Found value ({value}) at index: {_}")
                return
            temp = temp.next
        print("[!] Could not find the target Value")

    def setValueByIndex(self, value, index):
        if index < 0 or index > self.length - 1:
            print(f"[!] Invalid Index (Out of range Index): {index}")
        elif value is None:
            print(f"[!] Invalid Value{value}")
        else:
            temp = self.head
            i = 0
            while i < index:
                temp = temp.next
                i += 1
            temp.value = value

    def insertByIndex(self, value, index):
        if index < 0 or index > self.length:
            print(f"[!] Invalid Index (Out of range Index): {index}")
            return
        elif index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            # Method #1:
            # temp = self.head
            # i = 0
            # while i < index - 1:
            #     temp = temp.next
            #     i += 1
            # Method 2:
            temp = self.getByIndex(index=index - 1)
            new_node = Node(value)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1

    def removeByIndex(self, index):
        if index < 0 or index > self.length - 1:
            print(f"[!] Invalid Index (Out of range Index): {index}")
        elif index == 0:
            self.popFirst()
        elif index == self.length:
            self.pop()
        else:
            temp = self.getByIndex(index - 1)
            temp.next = temp.next.next

    def reverse(self):
        temp = self.head
        self.head, self.tail = self.tail, self.head
        after = temp.next
        before = None  # Retuen this for accessing reversed linked list
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


if __name__ == "__main__":
    my_list = LinkedList(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    my_list.append(5)
    my_list.append(6)
    my_list.print_list()
    my_list.reverse()
    my_list.print_list()
