class Car:
    is_police = False

    def __init__(self, name, color, speed=0):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self, speed):
        self.speed = speed
        print(f"{self.name} поехала со скоростью {self.speed} км/ч")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self, direction):
        directionName = ['налево', 'направо', 'разворот']
        print(f"{self.name} повернула: {directionName[direction]}")

    def show_speed(self):
        print(f"Скорость машины {self.name}: {self.speed} км/ч")


class TownCar(Car):
    def show_speed(self):
        if(self.speed > 60):
            excess = self.speed - 60
            print(f"Превышена скорость на {excess} км/ч")
        else:
            print(f"Скорость машины {self.name}: {self.speed} км/ч")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if(self.speed > 40):
            excess = self.speed - 40
            print(f"Превышена скорость на {excess} км/ч")
        else:
            print(f"Скорость машины {self.name}: {self.speed} км/ч")


class PoliceCar(Car):
    is_police = True


car_1 = TownCar('Opel', 'Black')
car_2 = SportCar('Mazda', 'Red')
car_3 = WorkCar('BMW', 'Black', 20)
car_4 = PoliceCar('Lada', 'Blue')

print(car_1.name)
print(car_1.speed)
print(car_2.color)
print(car_2.is_police)
print(car_3.speed)
print(car_4.is_police)

car_1.go(60)
car_1.stop()


car_2.go(50)
car_2.turn(1)

car_3.go(70)
car_3.show_speed()


car_4.go(150)
car_4.show_speed()


