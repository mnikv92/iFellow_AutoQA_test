import random


def min_max_mean() -> None:
    # создаю пустой список
    random_lst = []

    # задаю случайный размер массива от 2 до 10
    n = random.randint(2, 10)

    # заполняю список n числами от 0 до 1 включительно
    for i in range(n):
        random_lst.append(random.uniform(0, 1))

    print(random_lst)

    lst_max = max(random_lst)  # наибольший член массива
    lst_min = min(random_lst)  # наименьший член массива
    lst_mean = sum(random_lst) / n  # среднее значение членов массива

    print(f'Максимальное значение: {lst_max}')
    print(f'Минимальное значение: {lst_min}')
    print(f'Среднее значение: {lst_mean}')


min_max_mean()
