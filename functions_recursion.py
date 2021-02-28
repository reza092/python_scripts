# def count7(N):
    # '''
    # N: a non-negative integer
    # '''
    # count = []
    # while N > 10:
    #     if N%10 == 7:
    #         count.append(N)
    #     N = int(N/10)
        
    # else:
    #     if N == 7:
    #         count.append(N)
    #     else:
    #         pass
    # return len(count)
    
    # return count(N)
    
# def count7(N):
#     return counter(N,7)

# counts = 0

# def counter(N,y=7):
    
#     global counts
    
#     if N<10:
#         if N == 7:
#             counts +=1
#             return counts
        
#         else:
#             return counts
        
#     elif N%10==7:
#         counts +=1
#         return counter((N//10))
    
#     else:
#         return counter((N//10))

def count7(N):
    if N<10 and N!= 7:
        return 0
    elif N ==7:
        return 1
    elif N%10==7:
        return 1 + count7(N//10)
    else:
        return count7(N//10)
                    
            
# Recursion
# unless we call it for infinite time
    # an alternative of looping
    # multiply a*b by addition
# breaks down the problem into smaller repititive cases
# keep reducing until reach a simple case of direct solution


## def mult(a,b):
#     """
    
#     Parameters
#     ----------
#     a : positive integer.
#     b : positive integer.

#     Returns a * b
#     -------
#     recursion yield multiplication.

#     """
#     # BASE CASE
#     # if b == 1:
#     #     return a
    
#     # # RECURSIVE STEP
#     # else:
#     #     return a + mult(a, b-1)
    
# # Recursive function scope example
#     # GLOBAL scope
#     # BOUND code defining/method to make the problem smaller
    
#     # each recursive call to a function creates its own scope/environment
#     # binding of variables in a scope is not changed by recursive call
#     # flow of control passes back to previous scope once function call returns value
    


    
    
    
    
    
    
    
    
    