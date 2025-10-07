from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Using the dummy node to cover all the cases.
        dummy=ListNode(0,head)
        prev=dummy
        group_size=1
        while head:
            # Iterating for each group with the size group_size
            count=0
            tail=head
            while tail and count<group_size:
                tail=tail.next
                count+=1
            if count%2==0:
                prev.next=self.reverse_linked_list(head=head,count=count)
                prev=head
            else:
                prev=head
                for i in range(count-1):
                    prev=prev.next
            head=tail
            group_size+=1
        return dummy.next
    def reverse_linked_list(self, head, count):
        prev=None
        curr=head
        while count:
            aux_temp=curr.next
            curr.next=prev
            prev=curr
            curr=aux_temp
            count-=1
        head.next=curr
        return prev


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
    my_lst=[]
    while True:
        num=int(input("Type here a number value: "))
        if num==400:
            break
        my_lst.append(num)
    head=build_linked_list(values=my_lst)
    # print_linked_list(head=head)
    sol=Solution()
    head_result=sol.reverseBetween(head=head,left=left,right=right)
    print_linked_list(head=head_result)