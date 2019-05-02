import closure

if __name__ == "__main__":
    n = 10
    fib = closure.fib_closure(n)
    for i in range(n):
        print(fib(n), end=' ')
