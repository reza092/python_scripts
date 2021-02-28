def dot_product(listA,listB):
    sum = 0
    test = zip (listA,listB)
    for x,y in test:
        sum = sum + x*y
        
    return sum

listA = [1, 2, 3]
listB = [4,5,6]

A = dot_product(listA, listB)
print(A)