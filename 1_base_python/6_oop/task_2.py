class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self, mass_metr, depth):
        print(self._length * self._width * mass_metr * depth / 1000)


road_1 = Road(30, 2000)
road_1.calc_mass(15, 10)