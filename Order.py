class Order:

    order_counter = 0

    def __init__(self, computers):
        Order.order_counter += 1
        self._orderId = Order.order_counter
        self._computers = computers


    def add_computer(self, computer):
        self._computers.append(computer)

    def __str__(self):
        computers_str = ""
        for computer in self._computers:
            computers_str += computer.__str__()


        return f''' 
        Order: {self._orderId}
        Computers: {computers_str}
'''