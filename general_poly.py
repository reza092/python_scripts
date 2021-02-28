def general_poly(a,b):
    sum = 0
    for (i,num) in enumerate(a):
        sum = a[i]*(b**((len(a)-1)-i)) + sum
        print(sum)
    return sum

y = general_poly([1,2,3,4], 10)