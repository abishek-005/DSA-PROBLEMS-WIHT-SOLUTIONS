class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
def print_list(head):
    if head:
        print(head.value, end='')
        print_list(head.next)
    else:
        print() # Print newline at the end
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print("Linked list:")
print_list(head)
print("---------------------")
print("Reversing the linked list:")
def reverse_list(head):
    if not head or not head.next:
        return head
    new_head = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return new_head
# Reverse the list
new_head = reverse_list(head)
print_list(new_head)
