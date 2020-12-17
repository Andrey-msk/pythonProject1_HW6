#1
'''
 Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
  Атрибут реализовать как приватный.
   В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
    Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
     третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только
      в указанном порядке (красный, желтый, зеленый).
       Проверить работу примера, создав экземпляр и вызвав описанный метод.
'''
from time import sleep

class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор переключается \n '
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(3)
            i += 1

TrafficLight = TrafficLight()
TrafficLight.running()

2

class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width

class MassCount(Road):
    def __init__(self, _length, _width, volume):
        super().__init__(_length, _width)
        self.volume = volume

r = MassCount(25, 10000, 125)
print(r.mass())

3

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

a = Position('Denis', 'Monson', 'Trainer', 80000, 20000)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())

4

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turned right'

    def turn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car'
        else:
            return f'Speed of {self.name} is normal for town car'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for work car'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'

bmw = SportCar(100, 'Green', 'Bmw', False)
pegout = TownCar(30, 'Yellow', 'Pegout', False)
citroen = WorkCar(70, 'Black', 'Citroen', True)
mercedes = PoliceCar(110, 'White',  'Mercedes', True)
print(citroen.turn_left())
print(f'When {pegout.turn_right()}, then {bmw.stop()}')
print(f'{citroen.go()} with speed exactly {citroen.show_speed()}')
print(f'{citroen.name} is {citroen.color}')
print(f'Is {bmw.name} a police car? {bmw.is_police}')
print(f'Is {citroen.name}  a police car? {citroen.is_police}')
print(bmw.show_speed())
print(pegout.show_speed())
print(mercedes.police())
print(mercedes.show_speed())

5

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'

class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки ручкой'

class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки карандашом'

class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки маркером'

pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())