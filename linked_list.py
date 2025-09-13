class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """
    def __init__(self, data):
        """
        TODO:
        - Assign the provided 'data' to an instance variable.
        - Initialize 'next' to None.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    A simple linked list that holds Node objects and performs operations using recursion.
    """
    
    def __init__(self):
        """
        TODO:
        - Initialize 'head' to None to represent an empty list.
        """
        self.head = None

    def insert_at_front(self, data):
        """
        TODO:
        - Create a new Node with 'data'.
        - Insert it at the front of the list (head).
        - Update 'head' to the new node.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        (Optional) TODO:
        - Create a new Node with 'data'.
        - Traverse to the end of the list.
        - Set the last node's 'next' reference to the new node.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def recursive_sum(self):
        """
        TODO:
        - Use recursion to sum all node data in the list.
        - Provide a helper function that:
          1. Checks if the current node is None, and returns 0 if so.
          2. Otherwise, returns node.data + recursive call on node.next.
        - Return the total sum.
        """
        def _recursive_sum_helper(node):
            # Base case: if node is None, return 0
            if node is None:
                return 0
            # Recursive case: return current node's data + sum of rest
            return node.data + _recursive_sum_helper(node.next)
        
        return _recursive_sum_helper(self.head)

    def recursive_reverse(self):
        """
        TODO:
        - Reverse the list in-place using recursion.
        - Possible approach:
          1. Use a helper function that accepts 'prev' and 'current'.
          2. Base case: if 'current' is None, set 'head' to 'prev' (new head).
          3. Otherwise, swap pointers and recurse.
        - Update 'head' to the returned new head.
        """
        def _recursive_reverse_helper(prev, current):
            # Base case: if current is None, prev is the new head
            if current is None:
                return prev
            
            # Store the next node before we lose it
            next_node = current.next
            # Reverse the link
            current.next = prev
            # Recurse with the next pair
            return _recursive_reverse_helper(current, next_node)
        
        self.head = _recursive_reverse_helper(None, self.head)

    def recursive_search(self, target):
        """
        TODO:
        - Search for if 'target' is found, otherwise False, using recursion.
        - Provide a helper function that:
          1. Returns False if the current node is None.
          2. Returns True if current node's data == target.
          3. Otherwise, recurse on the next node.
        """
        def _recursive_search_helper(node, target):
            # Base case: if node is None, target not found
            if node is None:
                return False
            # Base case: if current node's data matches target
            if node.data == target:
                return True
            # Recursive case: search in the rest of the list
            return _recursive_search_helper(node.next, target)
        
        return _recursive_search_helper(self.head, target)

    def display(self):
        """
        TODO:
        - Print the contents of the list for debugging.
        - Traverse from 'head' and collect each node's data.
        - Format output as 'val -> val -> val -> None' or similar.
        """
        if not self.head:
            print("Empty list")
            return
        
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        
        print(" -> ".join(result) + " -> None")