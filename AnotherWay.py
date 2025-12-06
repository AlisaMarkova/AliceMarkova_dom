def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f'Функция {func.__name__} была вызвана {wrapper.calls} раз')
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper

@count_calls
def my_function(r):
    print('Вызов функции')

print(my_function(3))
my_function()
my_function()