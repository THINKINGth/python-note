# 闭包
def fib_closure(limit):
    i, f0, f1 = 0, 1, 1

    def generator():
        nonlocal i, f0, f1
        if i > limit:
            return
        num = f1
        f0, f1 = f0 + f1, f0
        return num
    return generator
