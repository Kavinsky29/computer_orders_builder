from Keyboard import Keyboard
from Mouse import Mouse
from Monitor import Monitor

class Computer:

    computerCount = 0

    def __init__(self, name, monitor, keyboard, mouse):
        Computer.computerCount += 1
        self._computerId = Computer.computerCount
        self._name = name
        self._monitor = monitor
        self._keyboard = keyboard
        self._mouse = mouse


    def __str__(self):
        return f'''
        {self._name}: {self._computerId}
        Monitor: {self._monitor}
        Keyboard: {self._keyboard}
        Mouse: {self._mouse}
'''

if __name__ == '__main__':
    keyboard1 = Keyboard("Logitech", "Bluetooth")
    mouse1 = Mouse("HP", "USB")
    monitor1 = Monitor("Alaska", 15)
    computer1 = Computer("Dell", monitor1, keyboard1, mouse1)
    print(computer1)
    keyboard2 = Keyboard("HyperX", "USB")
    mouse2 = Mouse("Logitech", "USB")
    monitor2 = Monitor("Sony", 30)
    computer2 = Computer("Compaq", monitor2, monitor2, keyboard2)
    print(computer2)