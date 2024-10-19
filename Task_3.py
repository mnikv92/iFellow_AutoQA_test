class BaseConverter:
    def __init__(self, temperature: float, scale: object):
        self.temperature = temperature
        self.scale = scale

    def convert(self) -> float:
        if self.scale == 'K' or self.scale == 'К':
            return self.temperature + 273.15
        elif self.scale == 'F':
            return self.temperature * 1.8 + 32
        else:
            raise ValueError(f'Неизвестные единицы измерения: {self.scale}')

    def show_temp(self) -> None:
        print(self.convert())


try:
    temperature = float(input('Введите температуру в градусах Цельсия: '))
    scale = input(
        'Выберите, в какие единицы измерения произвести конвертацию: \
"К" - в Кельвины, "F" - в Фаренгейты: ')
    temp_conv = BaseConverter(temperature, scale)
    temp_conv.show_temp()

except ValueError as err:
    print(err)