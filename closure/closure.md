# closure

### 基本原理

### 基本程序结构
>   定义一个函数f，其中定义若干局部变量构成f的局部状态。_在f里定义一个使用非局部状态的局部函数（这使得该函数依赖于调用f时创建的局部名字空间）_。f在建立起所需局部状态后返回其中定义的局部函数。调用这样的f建立起的结构就是闭包，每次调用建立一个新闭包，这种函数可称为**闭包函数**。由于F可以有参数，建立闭包时使用具体实参，创建的闭包与实参有关。

引入了非局部状态（ nonlocal i, f0, f1）
```python
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
```
```
打印结果：
D:\Anaconda\envs\python-note\python.exe D:/Anaconda/envs/python-note/closure/closure-test.py
1 1 2 3 5 8 13 21 34 55 
Process finished with exit code 0
```

只使用局部状态变量
```python
def fib_closure(limit):
    def generator():
        i, f0, f1 = 0, 1, 1
        if i > limit:
            return
        num = f1
        f0, f1 = f0 + f1, f0
        return num
    return generator
```
```
打印结果：
D:\Anaconda\envs\python-note\python.exe D:/Anaconda/envs/python-note/closure/closure-test.py
1 1 1 1 1 1 1 1 1 1 
Process finished with exit code 0
```
