def reassign(list):
    list = [0, 1] # python does not change the value in function
    list[0] = 1
    list[1] = 2

    print(list);

def append (list):
    list.append(1) # python will add value to list 

list = [0]
reassign(list);
append(list)
listA = [0]
listB = listA
listB.append(1)
print("HelloWorld")