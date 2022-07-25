'''
1. Создать класс мотоциклы. И минимум два экземпляра класса. У этих экземпляров помимо атрибутов есть методы.
 Это увелечение скорости, уменьшение скорости и цвет.
 Максимальная скорость у каждого обьекта разные, меньше нуля скорость уменьшаться не может.
  Все три метода приватные, т.е. мы не можем изменять параметры за пределами класса напрямую.
2* По поводу методов скорости.
 Каждый раз вызывая метод увеличения скорости,
  скорость постоянно увеличивается от скорости заданной ранее вызванным методом (на энное кол-во км).
  Не заходя за максимум. Ну и уменьшение работает так же, только в обратную сторону.
'''
class Motorbike: # класс
    # создание класса мотоциклы
    wheel = 2
    transmission = "machinal"  #атрибуты класса
    seat = 1
    def set_motorbike(self, color, accelerate, braking):
        self.__color = color
        self.__accelerate = accelerate
        self.__braking = braking

    def bike(self):
        print("цвет: ", self.__color, ",увеличениие скорости: ", self.__accelerate, ",торможение: ", self.__braking )

sports = Motorbike() # экземпляр класаа 1
sports.set_motorbike("red", 120, 0)

tourer = Motorbike() # экземпляр класса 2
tourer.set_motorbike("blak", 90, 0)


scooter = Motorbike()# экземпляр класса 3
scooter.set_motorbike("blue", 60, 0)
scooter.wheel = 3
scooter.seat = 3
scooter.transmission = "automatic"

scooter.bike()
sports.bike()
tourer.bike()

print(sports.transmission)