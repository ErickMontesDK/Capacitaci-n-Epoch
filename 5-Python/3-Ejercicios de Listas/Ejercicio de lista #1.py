list = [1,5,3,5,7,1,6,5,4,7,8,5,1,2,2,5,8,1,2,5,6,9,4,2]
no_repeat_list = []

for item in list:
    if no_repeat_list.count(item)==0 : no_repeat_list.append(item)
    
print(no_repeat_list)