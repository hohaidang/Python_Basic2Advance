class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        return
    def has_value(self, value):
        return True if self.data == value else False;

class SingleLInkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        return
    def add_list_item(self, item):
        if not isinstance(item, ListNode):
            item = ListNode(item) # if item is a data like int, string,... add to node
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        return

    def list_length(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count = count + 1
            current_node = current_node.next
        return count

    def output_list(self):
        current_node = self.head;
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        return

node1 = ListNode(15)
node2 = ListNode(8.2)
node4 = ListNode("Berlin")
item3 = 7

track = SingleLInkedList()
for current_item in [node1, node2, item3, node4]:
    track.add_list_item(current_item);

track.output_list()