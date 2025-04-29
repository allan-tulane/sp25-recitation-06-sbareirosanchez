def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """    
    counts[n] += 1
    print(counts)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib_recursive(n-1, counts) + fib_recursive(n-2, counts)
    

n=10
counts=[0] * (n+1)
print("fib_top_down: ", fib_top_down(n,fibs))
def fib_top_down(n, fibs):
    if n == 0:
        return 0
    elif n == 1
        return 1 
elif n in fibs:
    return fibs[n]
else: 
    return fib_top_down(n-1, fibs)+fib_top_down(n-2, fibs)
    


def fib_bottom_up(n):
    fibs = [0] * (n+1)
    fibs[0] = 0 
    fibs[1]= 1
    for i in range(2, n + 1):
        fibs[i] = fibs[i - 1] + fibs [i-2]
    return fibs[n]




