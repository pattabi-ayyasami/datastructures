class Item:
    value = None
    next = None

    def __init__(self, data):
        self.data = data

    def display(self):
        print ( "Item: { " + str(self.data) + " }" )

class LinkList:
    first = None

    def is_empty(self):
        return self.first == None

    def insert_first(self, id):
        link = Item(id)
        link.next = self.first
        self.first = link

    def delete_first(self):
        temp = None
        if self.first != None:
            temp = self.first
            self.first = self.first.next
        return temp

    def find_item(self, key):
        current = self.first
        while current is not None:
            if current.data == key:
                return current
            current = current.next
        return None

    def delete_item(self, key):
        current = self.first

        if current is not None:
            if current.data == key:
                self.first = current.next
                current = None
                return

        prev = None
        while current is not None:
            if current.data == key:
                break

            prev = current
            current = current.next

        if current is None:  # key not found
            print "Key " + str(key) + " does not exist"
            return

        prev.next = current.next
        current = None

    def does_item_exist(self, key):
        temp = self.first
        while temp is not None:
            if temp.data == key:
                print "Key " + str(key) + " exists"
                return True
            temp = temp.next

        print "Key " + str(key) + " does not exist"
        return False

    def display(self):
        print ("List (first --> last:")
        current = self.first
        while current != None:
            current.display()
            current = current.next

    def reverse(self):
        prev = None
        current = self.first
        while current is not None:
            next = current.next
            current.next = prev

            prev = current
            current = next
        self.first = prev

    def get_nth_item(self, index):
        current = self.first
        count = 0
        while current is not None:
            if count == index:
                return current

            count += 1
            current = current.next

        print "No node at specifed index " + str(index) + " exists"
        return None

    def middle(self):

        if self.first is None:
            print "Empty list"
            return

        current = self.first
        next = current
        next_next = current

        even = True
        while next_next is not None:
            current = next
            next = current.next

            # advance the next_next by 2 positions
            if next_next.next is not None:
                next_next = next_next.next.next
            else:
                even = False
                next_next = None

        print "================================="
        print "Middle node(s) of the link list:"
        current.display_link()
        if even:
            next.display_link()
        print "================================="


    def detect_loop(self):
        slow_p = self.first
        fast_p = self.first

        while slow_p and fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                print "Detected loop in the list"
                return
        print "No loop detected in the list"

    def get_count(self):
        count = 0
        current = self.first

        while current:
            count += 1
            current = current.next

        print "# of nodes in the linked list: ", count
        return count
