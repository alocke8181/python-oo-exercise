"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,start):
        "Initalizes a serial with a given starting value"
        self.start = start
        self.val = start

    def generate(self):
        "Increments the value of the serial by one"
        self.val = self.val + 1
        return self.val - 1
    
    def reset(self):
        "Resets the value to the starting value"
        self.val = self.start
    
    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.val}>"

