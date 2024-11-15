# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# def addTwoNumbers(l1: ListNode, l2: ListNode) ->ListNode:
#     result_l = list()
#     length_1 = len(list(l1))
#     length_2 = len(list(l2))
#     if length_1 >= length_2:
#         z_part = 0
#         for i in range(length_2):
#             sum = l1[i] + l2[i] + z_part
#             z_part = 0
#             if sum < 10:
#                 result_l.append(sum)
#             else:
#                 rest = sum % 10
#                 result_l.append(rest)
#                 z_part = sum // 10
#         for i in range(length_2, length_1):
#             sum = l1[i] + z_part
#             z_part = 0
#             if sum < 10:
#                 result_l.append(sum)
#             else:
#                 rest = sum % 10
#                 result_l.append(rest)
#                 z_part = sum // 10
#         if z_part != 0:
#             result_l.append(z_part)
#     else:
#         result_l = addTwoNumbers(l2, l1)
#     return result_l
# l1 = ListNode()
# l2 = ListNode()
# l1 = [9,9,9,9,9,9,9]
# l2 = [9,9,9,9]
# print(addTwoNumbers(l1,l2))

# # Input: l1 = [2,4,3], l2 = [5,6,4]
# # Output: [7,0,8]
# # Explanation: 342 + 465 = 807.
# # Example 2:

# # Input: l1 = [0], l2 = [0]
# # Output: [0]
# # Example 3:

# # Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# # Output: [8,9,9,9,0,0,0,1]

# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         dummyHead = ListNode(0)
#         tail = dummyHead
#         carry = 0

#         while l1 is not None or l2 is not None or carry != 0:
#             digit1 = l1.val if l1 is not None else 0
#             digit2 = l2.val if l2 is not None else 0

#             sum = digit1 + digit2 + carry
#             digit = sum % 10
#             carry = sum // 10

#             newNode = ListNode(digit)
#             tail.next = newNode
#             tail = tail.next

#             l1 = l1.next if l1 is not None else None
#             l2 = l2.next if l2 is not None else None

#         result = dummyHead.next
#         dummyHead.next = None
#         return result
# x= input()
# y = str(x)
# x = list(y)

# x.reverse()

# z = ''.join(x)

# if  z == y:
#     print('True')
# else: 
#     print('False')
symbol = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
value = [1, 5, 10, 50, 100, 500, 1000]
x = 'LC'
val = 0
for i in range(len(x)):
    val += value[symbol.index(x[i])]
    if x[i] in ['I', 'X', 'C']:
        pass
    # if i != len(x) - 1:
    #     if symbol[symbol.index(x[i]) + 1] == x[i+1] or symbol[symbol.index(x[i]) + 2]==x[i+1]:
    #         tmp = - value[symbol.index(x[i])]
    #         val += tmp
    #     else:
    #         val += value[symbol.index(x[i])]    
    # else: 
    #     val += value[symbol.index(x[i])]

print(val)