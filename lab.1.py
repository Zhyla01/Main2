# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def __str__(self):
#         return f"{self.data} -> {self.next}"
#
# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def __str__(self):
#         return f"{self.head}"
#
#     def push_end(self, data):
#         new_node = Node(data)
#
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#             return
#
#         self.tail.next = new_node
#         self.tail = new_node
#
# data = SinglyLinkedList()
# data.push_end(1)
# data.push_end(2)
# data.push_end(3)
# print(data)

