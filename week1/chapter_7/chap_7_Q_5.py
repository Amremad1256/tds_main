def remove_duplicates_preserve_order(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

original_list = [1, 2, 2, 3, 4, 4, 5]
new_list = remove_duplicates_preserve_order(original_list)
print("List with duplicates removed:", new_list)