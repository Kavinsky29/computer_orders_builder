class Monitor:

    monitorCount = 0

    def __init__(self, brand, size):
        Monitor.monitorCount += 1
        self._monitorId = Monitor.monitorCount
        self._brand = brand
        self._size = size


    def __str__(self):
        return f" Monitor ID: {Monitor.monitorCount},  Monitor Brand: {self._brand},  Monitor Size: {self._size}"

if __name__ == "__main__":
    monitor1 = Monitor("Dell", 22)
    print(monitor1)
    monitor2 = Monitor("AOC", 45)
    print(monitor2)