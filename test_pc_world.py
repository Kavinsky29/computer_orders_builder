from Keyboard import Keyboard
from Mouse import Mouse
from Monitor import Monitor
from Computer import Computer
from Order import Order

keyboard1 = Keyboard("Logitech", "Bluetooth")
mouse1 = Mouse("HP", "USB")
monitor1 = Monitor("Alaska", 15)
computer1 = Computer("Dell", monitor1, keyboard1, mouse1)

keyboard2 = Keyboard("HyperX", "USB")
mouse2 = Mouse("Logitech", "USB")
monitor2 = Monitor("Sony", 30)
computer2 = Computer("Compaq", monitor2, monitor2, keyboard2)

keyboard3 = Keyboard("Gamer", "USB")
mouse3 = Mouse("Gamer", "Bluetooth")
monitor3 = Monitor("Panasonic", 34)
computer3 = Computer("Gamer", monitor3, keyboard3, mouse3)

computers1 = [computer1, computer2]
order1 = Order(computers1)
# print(order1)
order1.add_computer(computer3)
print(order1)

computers2 = [computer2, computer3]
order2 = Order(computers2)
print(order2)