# Find the maximum number from the list
def max_num_in_list(l):
    max1 = l[0]
    for i in l:
        if i > max1:
            max1 = i
    return max1




list1 = [1, 2, -8, 0]

print(max_num_in_list(list1))

