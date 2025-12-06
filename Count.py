def counter(func):
    def wrapper(*args):
        func.count += 1
        print(f'Функцию {func.__name__} вызывали {func.count} ')
        return func(*args)
    func.count = 0
    return wrapper


@counter
def f(x, y):
    return x * y


@counter
def g(x):
    return 10 * x


@counter
def h(y):
    return y ** 2


print(f(3, 55))
print(g(2))
print(g(5))
print(h(3))
print(h(12))
print(h(33))


def print_statistics():
    print('Сколько раз вызывались функции: ')
    for func, count in counter:
        print(f'{func}: {count} раз')
    print()


def main():
    func = {
        '1': f,
        '2': g,
        '3': h,
        '4': print_statistics
    }
    if __name__ == "__main__":
        main()

    print('Выберите функцию (1-3) или 4 чтобы узнать, сколько раз вызывались функции ')

    while True:
        choice = input('Ваш выбор: ')
        if choice in func:
            func[choice]()
        elif choice == '4':
            print_statistics()
        else:
            print('Ошибка ввода. Выберите функцию (1-3) или 4 чтобы узнать, сколько раз вызывались функции')


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Программа завершена")




