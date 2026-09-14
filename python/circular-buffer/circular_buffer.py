"""Implement a Circular Buffer"""

# pylint: disable=missing-function-docstring

class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class CircularBuffer:  # pylint: disable=missing-class-docstring
    def __init__(self, capacity):
        self.buffer = []
        self.capacity = capacity

    def read(self):
        if not self.buffer:
            raise BufferEmptyException("Circular buffer is empty")
            
        return self.buffer.pop(0)

    def write(self, data):
        if len(self.buffer) < self.capacity:
            self.buffer.append(data)
        else:
            raise BufferFullException("Circular buffer is full")

    def overwrite(self, data):
        if len(self.buffer) == self.capacity:
            self.buffer.pop(0)
        self.buffer.append(data)

    def clear(self):
        self.buffer = []
