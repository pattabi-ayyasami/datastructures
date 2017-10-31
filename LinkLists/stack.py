from link_list import Item, LinkList

class Stack(LinkList):
    def peek(self):
        if self.is_empty():
            return None
        return self.first

    def pop(self):
        if self.is_empty():
            return None
        return self.delete_first()

    def push(self, item):
        self.insert_first(item)
        return item


def main():
    stack = Stack()
    stack.push(2)
    stack.push(4)
    stack.push(6)
    stack.push(8)
    stack.display()

    top_item = stack.peek()
    top_item.display()

    item = stack.pop()
    item.display()

    item = stack.pop()
    item.display()

    stack.display()

if __name__ == "__main__":
    main()