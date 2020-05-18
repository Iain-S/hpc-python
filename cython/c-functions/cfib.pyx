cpdef int fibonacci(int n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


cpdef int recurse(int n):
    if n == 10000:
        print('done: ', n)
        return n
    else:
        recurse(n+1)
