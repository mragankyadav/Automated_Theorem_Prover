# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy=ListNode()
        dummy.next=head
        front=back=prev=ListNode()
        prev=dummy
        back=head
        front=head.next
        temp=ListNode()
        while(front!=None):
            temp=front.next
            front.next=back
            back.next=temp
            prev.next=front
            temp2=front
            front=back
            back=front
            if(front.next!=None):
                prev=front
                back=front.next
                front=back.next
            else:
                front=None



