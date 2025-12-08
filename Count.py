cnt = {}

def counter(func):
    def wrapper(*args):
        cnt[func.__name__] += 1
        print(f'Функцию {func.__name__} вызывали {cnt[func.__name__]} ')
        return func(*args)

    cnt[func.__name__] = 0
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


def print_statistics():
    print('Сколько раз вызывались функции: ')
    for func_name, count in cnt.items():
        print(f'{func_name}: {count} раз')
    print()


def main():
    func = {
        '1': f,
        '2': g,
        '3': h,
        '4': print_statistics
    }

    print('Выберите функцию (1-3) или 4 чтобы узнать, сколько раз вызывались функции ')

    while True:
        choice = input('Ваш выбор: ')
        if choice == '4':
            print_statistics()
        elif choice in func:
            try:
                if choice == '1':
                    x = float(input('Введите значение x: '))
                    y = float(input('Введите значение y: '))
                    result = func[choice](x, y)
                    print(f'Результат: {result}')
                else:
                    arg = float(input('Введите значение аргумента: '))
                    result = func[choice](arg)
                    print(f'Результат: {result}')
            except ValueError:
                print('Необходимо ввести число')
        else:
            print('Ошибка ввода. Выберите функцию 1, 2, 3 или 4.')


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Программа завершена")





