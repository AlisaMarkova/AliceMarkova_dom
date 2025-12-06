def counter(func):
    def wrapper(*args):
        func.count += 1
        print(f'Функцию {func.__name__} вызывали {func.count} ')
        return func(*args)
    func.count = 0
    return wrapper


@counter
def f(x, y):
    return x + y


@counter
def g(x):
    return 1 / (x ** 2 + 1)


@counter
def h(y):
    return 5 ** y


print(f(55, 77))
print(g(2))
print(g(-2))
print(h(3))
print(h(12))
print(h(33))
print(h(100))

