from Device_Input import *

class Keyboard(DeviceInput):

    keyboardCounter = 0

    def __init__(self, brand, inputType):
        super().__init__(brand, inputType)
        Keyboard.keyboardCounter += 1
        self._keyboardId = Keyboard.keyboardCounter

    def __str__(self):
        return f"Keyboard ID: {Keyboard.keyboardCounter},  Brand: {self.brand},  Input Type: {self.inputType}"

if __name__ == "__main__":

    keyboard1 = Keyboard("Logitech", "USB")
    print(keyboard1)
    keyboard2 = Keyboard("HP", "Serial")
    print(keyboard2)