__author__ = 'bouilli'
def reverseList(head):
    tmp = None
    curr = head
    while (curr != None and curr.next != None):
        tmp = curr.next.next
        curr.next.next = head
        head = curr.next
        curr.next = tmp
    return head
