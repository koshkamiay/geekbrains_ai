class Stationery:
    title = 'Канцелярская принадлежность'

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    title = "Ручка"

    def draw(self):
        print("Ручка начинает рисовать")


class Pencil(Stationery):
    title = "Карандаш"

    def draw(self):
        print(f"{self.title} начинает создавать шедевр")


class Handle(Stationery):
    title = "Маркер"

    def draw(self):
        print("Выделяем важное предложение")


my_pen = Pen()
my_pencil = Pencil()
my_handle = Handle()

my_pen.draw()
my_pencil.draw()
my_handle.draw()

