def quicksort(list):
    left=[]
    right=[]
    equal=[]

    if len(list) > 1:
        pivot=list[-1]
        for i in list:
            if list[i] < pivot:
                left.append(list[i])
            elif list[i] == pivot:
                equal.append(list[i])
            elif list[i] > pivot:
                right.append(list[i])
        return quicksort(left) + equal + quicksort(right)
    else:
        return list

print(quicksort([3,4,1,6,8,10,-22,0]))
