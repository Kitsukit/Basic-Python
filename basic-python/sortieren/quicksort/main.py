def quicksort(list):
    left=[]
    right=[]
    equal=[]

    if len(list) > 1:
        pivot=list[-1]
        for i in list:
            if x < pivot:
                left.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                right.append(x)
        return quicksort(left) + equal + quicksort(right)
    else:
        return list

print(quicksort([3,4,1,6,8,10,-22,0]))
