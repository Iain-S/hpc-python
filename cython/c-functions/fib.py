def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


def recurse(n):
    if n == 1000:
        print('done')
    else:
        recurse(n+1)
