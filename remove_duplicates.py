num_list = [1,3,4,5]
dup_found = False
new_list = []
for num in num_list:
    if num not in new_list:
        new_list.append(num)
        dup_found = True
if dup_found:
    print(new_list)
else:
    print(num_list)