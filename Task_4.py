def corner_calc(hours, minutes) -> int:
    # начальное положение стрелок определяю как 0 часов 0 минут

    # угол поворота минутной стрелки
    minutes_angle = 6 * minutes

    # угол поворота часовой стрелки учитывает кол-во часов и минут
    hours_angle = 30 * hours + 30 * minutes / 60

    # модуль (abs) введен чтобы абстрагироваться от направления вращения
    between_angle = abs(hours_angle - minutes_angle)
    return between_angle


def hours_check(hours: int):

    # проверка введенного значения часов
    if hours > 24 or hours < 0:
        print('Введите корректное значение часов')
        return
    elif 12 <= hours < 24:
        hours -= 12
    elif hours == 24:
        hours = 0
    return hours


def minutes_check(minutes):
    # проверка введенного значения минут
    if minutes >= 60 or minutes < 0:
        print('Введите корректное значение минут')
        return

    return minutes


try:
    hours = int(input('Введите часы: '))
    minutes = int(input('Введите минуты: '))

    hours = hours_check(hours)
    minutes = minutes_check(minutes)
    print(
        f'Угол между часовой и минутной стрелками составил \
{corner_calc(hours, minutes)}')
except Exception as ex:
    print(f'An error occured. Message: {ex}')