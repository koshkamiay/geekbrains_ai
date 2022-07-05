import time


class TrafficLight:
    _color = 0
    _color_name = ['красный', 'желтый', 'зеленый']
    _color_delay = [7, 2, 4]

    def running(self, color=0):
        self._color = color

        while True:
            print(f'Cветофор переключился на {self._color_name[self._color]} свет')
            time.sleep(self._color_delay[self._color])
            if self._color == len(self._color_name) - 1:
                self._color = 0
            else:
                self._color += 1


my_traffic_light = TrafficLight()
my_traffic_light.running()