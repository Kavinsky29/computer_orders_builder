class DeviceInput:

    def __init__(self, brand, inputType):
        self._inputType = inputType
        self._brand = brand

    def __str__(self):
        return f"Brand: {self._brand}, Input Type: {self._inputType}"

    @property
    def inputType(self):
        return self._inputType

    @inputType.setter
    def inputType(self, inputType):
        self._inputType = inputType


    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

# DeviceInput1 = DeviceInput("USB", "Acer")
# print(DeviceInput1)