class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f"Сотрудник {self.name} {self.surname}")

    def get_total_income(self):
        full_income = self._income['wage'] + self._income['bonus']
        print(f"Зарплата с учетом премии: {full_income}")


worker_1 = Position('Иван', 'Иванов', 'Инженер', 20000, 5000)
print(worker_1.position)
worker_1.get_full_name()
worker_1.get_total_income()

