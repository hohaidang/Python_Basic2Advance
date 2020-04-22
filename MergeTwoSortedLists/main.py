class ListNode:
    def __init__(self, data):
        self.val = data;
        self.next = None;

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def addNode(self, item):
        if not isinstance(item, ListNode):
            item = ListNode(item)
        if self.head is None:
            self.head = item;
        else:
            self.tail.next = item;
        self.tail = item;

def mergeLinkedListRecursion(l1, l2):
    if l1 is None:
        return l2;
    if l2 is None:
        return l1;
    if l1.val < l2.val:
        l1.next = mergeLinkedListRecursion(l1.next, l2)
        return l1
    else:
        l2.next = mergeLinkedListRecursion(l1, l2.next)
        return l2

def mergeLinkedLIstIterate(l1, l2):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif (l1 is None) and (l2 is None):
        return []
    retList = SingleLinkedList()

    while((l1 is not None) and (l2 is not None)):
        if l1.val < l2.val:
            retList.addNode(l1.val)
            l1 = l1.next
        elif l2.val < l1.val:
            retList.addNode(l2.val)
            l2 = l2.next
        else:
            retList.addNode(l1.val)
            retList.addNode(l2.val)
            l1 = l1.next
            l2 = l2.next
        if l1 is None:
            retList.tail.next = l2
            break
        elif l2 is None:
            retList.tail.next = l1
            break

    return retList



l1 = SingleLinkedList()
l2 = SingleLinkedList()
l1.addNode(1)
l1.addNode(2)
l1.addNode(3)
l1.addNode(5)
l2.addNode(2)
l2.addNode(4)
l2.addNode(6)
# l1 = 1->2->3->5
# l2 = 2->4->6
# merge1 = mergeLinkedListRecursion(l1.head, l2.head)
merge = mergeLinkedLIstIterate(l1.head, l2.head)
print("End Program")