list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
new_list = []
for num in list1:
    if num % 2 == 1:
        new_list.append(num)
for num in list2:
    if num % 2 == 0:
        new_list.append(num)

print(new_list)
