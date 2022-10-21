from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def calc(self):
        pass


class Coat(Clothes):
    def __init__(self, title, size):
        super().__init__(title)
        self._size = size

    def calc(self):
        material = self._size/6.5 + 0.5
        return round(material, 2)

    @property
    def size(self):
        return self._size


class Suit(Clothes):
    def __init__(self, title, height):
        super().__init__(title)
        self._height = height

    def calc(self):
        material = self._height * 2 + 0.3
        return round(material, 2)

    @property
    def height(self):
        return self._height


coat_1 = Coat('Мое первое пальто', 20)
print(coat_1.size)
print(coat_1.calc())

suit_1 = Suit('Свадебный костюм', 1.89)
print(suit_1.height)
print(suit_1.calc())

print(coat_1.calc() + suit_1.calc())