my_list = [1, 2, 3, 4, 5]
my_set = {1, 2, 3, 4, 5}

while True:
    print("\n1. Add Element")
    print("2. Remove element")
    print("3. Combine two lists")
    print("4. Find intersection of two sets")
    print("5. Find Difference of two sets")
    print("6. Find union of two sets")
    print("7. Check element in a list or set")
    print("8. Get length of a list or set")
    print("9. Sort a list")
    print("10. Clear a list or set")
    print("11. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice =='1':
        new_element=int(input("Enter the element to add:- "))
        my_list.append(new_element)
        my_set.add(new_element)
        print("List after adding element:- ",my_list)
        print("Set after adding element:- ",my_set)
    elif choice =='2':
        remove_element=int(input("Enter the element to remove:- "))
        if remove_element in my_list:
            my_list.remove(remove_element)
        if remove_element in my_set:
            my_set.remove(remove_element)
        print("List after remove element:- ", my_list)
        print("Set after remove element:-  ", my_set)
    elif choice =='3':
        other_list=[6,7,8]
        Combined_list=my_list+other_list
        print("Combined list:- ",Combined_list)
    elif choice =='4':
        other_set={4,5,10}
        intersection_set=my_set.intersection(other_set)
        print("intersection set:- ",intersection_set)
    elif choice =='5':
        others_set={10,5,8,2}
        difference_set=my_set.difference(others_set)
        print("Difference set:- ",difference_set)
    elif choice == '6':
        other_set = {9, 7, 8}
        union_set = my_set.union(other_set)
        print("Union set: ", union_set)
    elif choice == '7':
        element_to_check = int(input("Enter the element to check: "))
        if element_to_check in my_list:
            print("Element is in list")
        if element_to_check in my_set:
            print("Element is in set")
    elif choice == '8':
        print("Length of list: ", len(my_list))
        print("Length of set: ", len(my_set))
    elif choice == '9':
        my_list.sort()
        print("Sorted list: ", my_list)
    elif choice == '10':
        my_list.clear()
        my_set.clear()
        print("List after clearing: ", my_list)
        print("Set after clearing: ", my_set)
    else:
        exit()
    
