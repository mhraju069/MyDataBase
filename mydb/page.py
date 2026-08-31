PAGE_SIZE = 4096


class Page:
    def __init__(self):
        self.data = bytearray(PAGE_SIZE)

    def write(self, data: bytes):
        if len(data) > PAGE_SIZE:
            raise ValueError("Data is too large for page")

        self.data[:len(data)] = data

    def read(self) -> bytes:
        return bytes(self.data)