# Remove the duplicates from the list

a = [10, 20, 30, 20, 10, 40, 50, 40, 60, 40]
duplicate_list = set()
unique_list = []
for i in a:
    if i not in duplicate_list:
        unique_list.append(i)
        duplicate_list.add(i)
print(unique_list)