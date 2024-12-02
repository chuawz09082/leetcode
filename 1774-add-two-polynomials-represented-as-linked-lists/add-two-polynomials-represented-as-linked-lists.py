# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        """
        Adds two polynomials represented as linked lists.

        Args:
        poly1 (PolyNode): The head of the first polynomial linked list.
        poly2 (PolyNode): The head of the second polynomial linked list.

        Returns:
        PolyNode: The head of the resulting polynomial linked list after addition.
        """

        # Initialize pointers for traversing both polynomial linked lists
        current1 = poly1
        current2 = poly2

        # Skip nodes with equal powers and zero combined coefficients
        while current1 and current2 and current1.power == current2.power and current1.coefficient + current2.coefficient == 0:
            current1 = current1.next
            current2 = current2.next

        # Handle cases where either list is completely traversed
        if not current1 and not current2:
            return None  # Both lists are empty after removing zero terms
        elif not current2:
            return current1  # Only the first list remains
        elif not current1:
            return current2  # Only the second list remains

        # Handle the case where the first nodes have the same power
        if current1 and current2 and current1.power == current2.power:
            newNode = PolyNode(current1.coefficient + current2.coefficient, current1.power)
            current1 = current1.next
            current2 = current2.next
        elif current1.power > current2.power:  # First list has higher power
            newNode = PolyNode(current1.coefficient, current1.power)
            current1 = current1.next
        else:  # Second list has higher power
            newNode = PolyNode(current2.coefficient, current2.power)
            current2 = current2.next

        # Pointer to build the resulting polynomial linked list
        currentnew = newNode

        # Traverse both lists to combine terms
        while current1 or current2:
            if not current1:
                currentnew.next = current2  # Append remaining terms from the second list
                return newNode
            if not current2:
                currentnew.next = current1  # Append remaining terms from the first list
                return newNode

            # Skip nodes with equal powers and zero combined coefficients
            while current1 and current2 and current1.power == current2.power and current1.coefficient + current2.coefficient == 0:
                current1 = current1.next
                current2 = current2.next

            # Combine terms with the same power
            if current1 and current2 and current1.power == current2.power:
                currentnew.next = PolyNode(current1.coefficient + current2.coefficient, current1.power)
                current1 = current1.next
                current2 = current2.next
                currentnew = currentnew.next
            elif current1 and current2 and current1.power > current2.power:
                # Add term from the first list
                currentnew.next = PolyNode(current1.coefficient, current1.power)
                current1 = current1.next
                currentnew = currentnew.next
            elif current1 and current2 and current2.power > current1.power:
                # Add term from the second list
                currentnew.next = PolyNode(current2.coefficient, current2.power)
                current2 = current2.next
                currentnew = currentnew.next

        # Return the head of the new polynomial linked list
        return newNode

        
        