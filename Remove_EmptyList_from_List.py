#Program to remove the Empty list from the list

test_list = [12, 32, [], 43, [], 67, 87, 99, [], 32]
print("The Original list is : " + str(test_list))

result = [elements for elements in test_list if elements != []]
print("List after removing empty list", str(result))


