from Device_Input import *

class Mouse(DeviceInput):

    mouseCounter = 0

    def __init__(self, brand, inputType):
        super().__init__(brand, inputType)
        Mouse.mouseCounter += 1
        self._mouseId = Mouse.mouseCounter

    def __str__(self):
        return f"Mouse ID: {Mouse.mouseCounter}, Brand: {self.brand},  Input Type: {self.inputType}"

if __name__ == "__main__":

    mouse1 = Mouse("Alaska", "Bluetooth")
    print(mouse1)
    mouse2 = Mouse("Dell", "Serial")
    print(mouse2)