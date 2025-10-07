from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        it1=l1
        it2=l2
        go_1=0
        initial_sum=(it1.val+it2.val)
        if initial_sum>=10:
            go_1=initial_sum//10
        rest=initial_sum%10
        head=ListNode(rest)
        curr=head
        it1=it1.next
        it2=it2.next
        while it1 and it2:
            rest=(it1.val+it2.val)%10
            go_1=(it1.val+it2.val)//10
            curr.next=ListNode(head+go_1)
            curr=curr.next
            it1=it1.next
            it2=it2.next
        while it1:
            curr.next=ListNode(it1.next.val)
            curr=curr.next
            it1=it1.next
        while it2:
            curr.next=ListNode(it2.next.val)
            curr=curr.next
            it2=it2.next
        return head


def build_linked_list(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None
    head=ListNode(values[0])
    current=head
    for val in values[1:]:
        current.next=ListNode(val)
        current=current.next
    return head
def print_linked_list(head):
    if not head:
        return None
    result=[]
    curr=head
    while curr:
        result.append(str(curr.val))
        curr=curr.next
    print('->'.join(result))

if __name__=="__main__":
    my_lst1=[]
    while True:
        num=int(input("Type here a number value: "))
        if num==400:
            break
        my_lst1=[].append(num)
    my_lst2=[]
    while True:
        num=int(input("Type here a number value: "))
        if num==400:
            break
        my_lst2=[].append(num)
    head1=build_linked_list(values=my_lst1)
    head2=build_linked_list(values=my_lst1)

    # print_linked_list(head=head)
    sol=Solution()
    head_result=sol.addTwoNumbers(head1=head1,head2=head2)
    print_linked_list(head=head_result)