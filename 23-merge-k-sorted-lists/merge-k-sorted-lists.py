# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []  # A min-heap to store (value, index) pairs for efficient retrieval of the smallest value
        
        # Initialize the heap with the head of each non-empty linked list
        for i, listnode in enumerate(lists):
            if listnode:
                # Push the value of the node and its index in the lists array into the heap
                heappush(min_heap, (listnode.val, i))
                # Move the pointer to the next node in the list
                lists[i] = listnode.next

        # If the heap is empty after initialization, return None (no lists to merge)
        if not min_heap:
            return None
            
        # Pop the smallest element from the heap to start the merged list
        val, idx = heappop(min_heap)
        result = ListNode(val)  # Create the head of the result list
        current = result        # Pointer to the current node in the result list

        # If the list from which the smallest element was taken still has nodes, push the next node into the heap
        if lists[idx]:
            heappush(min_heap, (lists[idx].val, idx))
            lists[idx] = lists[idx].next
        
        # Process the remaining elements in the heap
        while min_heap:
            # Pop the smallest element from the heap
            val, idx = heappop(min_heap)
            # Append it to the result list
            current.next = ListNode(val)
            # If there are more nodes in the corresponding list, push the next node into the heap
            if lists[idx]:
                heappush(min_heap, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
            # Move the current pointer to the newly added node
            current = current.next
        
        return result  # Return the head of the merged sorted linked list
        