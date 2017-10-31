from link_list import Item, LinkList

def main():
    list = LinkList()
    list.insert_first(2)
    list.insert_first(4)
    list.insert_first(6)
    list.insert_first(8)
    list.insert_first(10)
    list.insert_first(12)

    list.display()
    list.get_count()

    '''

    list.first.next.next.next.next = list.first
    list.detect_loop()

    list.middle()

    node = list.get_nth_node(0)
    if node:
        node.display_link()

  
    list.reverse()
    list.display_list()


    list.delete_node(2)
    list.display_list()
    list.delete_node(60)

    list.does_node_exist(61)
    list.does_node_exist(4)

    node = list.find_node(4)
    if node is not None:
        node.display_link()

    list.delete_node(8)
    list.display_list()

    while not list.is_empty():
        link = list.delete_first()
        print "Deleted Link: "
        link.display_link()

    list.display_list()
    '''

if __name__ == "__main__":
    main()