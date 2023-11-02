def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst)-1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list

original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print("Reversed list:", reversed_list)