from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations
    like insertion, recursion-based sum, search, and reverse.
    """
    
    print("=== Linked Lists and Recursion Lab Demo ===\n")
    
    # TODO: 1) Create a LinkedList instance
    ll = LinkedList()
    print("1. Created an empty LinkedList")
    ll.display()
    print()
    
    # TODO: 2) Insert some sample data using insert_at_front or insert_at_end
    print("2. Inserting sample data...")
    ll.insert_at_front(10)
    ll.insert_at_front(20)
    ll.insert_at_front(30)
    ll.insert_at_end(5)
    print("Inserted: 30 (front), 20 (front), 10 (front), 5 (end)")
    print("Current list:")
    ll.display()
    print()
    
    # TODO: 3) Display the list to verify insertion
    print("3. List verification complete - see above display")
    print()
    
    # TODO: 4) Call recursive_sum and print the result
    print("4. Testing recursive sum...")
    total_sum = ll.recursive_sum()
    print(f"Sum of all elements: {total_sum}")
    print("Expected: 30 + 20 + 10 + 5 = 65")
    print()
    
    # TODO: 5) Call recursive_search with a target and print result
    print("5. Testing recursive search...")
    search_targets = [20, 100, 5, 30]
    for target in search_targets:
        found = ll.recursive_search(target)
        print(f"Search for {target}: {'Found' if found else 'Not found'}")
    print()
    
    # TODO: 6) Call recursive_reverse, then display the reversed list
    print("6. Testing recursive reverse...")
    print("List before reversal:")
    ll.display()
    
    ll.recursive_reverse()
    
    print("List after reversal:")
    ll.display()
    print()
    
    # Additional demonstration with a different list
    print("=== Additional Demo with Employee IDs ===")
    employee_list = LinkedList()
    
    # Simulate employee ID management
    employee_ids = [101, 205, 303, 442, 567]
    print(f"Adding employee IDs: {employee_ids}")
    
    for emp_id in employee_ids:
        employee_list.insert_at_end(emp_id)
    
    print("Employee roster (as linked list):")
    employee_list.display()
    
    print(f"Total of all employee IDs: {employee_list.recursive_sum()}")
    
    # Search for specific employee
    search_id = 303
    if employee_list.recursive_search(search_id):
        print(f"Employee ID {search_id} found in the roster ✓")
    else:
        print(f"Employee ID {search_id} not found in the roster ✗")
    
    print("\n=== Lab Complete! ===")