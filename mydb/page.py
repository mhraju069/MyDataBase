from .row import Row
PAGE_SIZE = 4096


class Page:
    def __init__(self, data=None):
        if data is None:
            self.data = bytearray(PAGE_SIZE)
        else:
            if len(data) != PAGE_SIZE:
                raise ValueError("Invalid page size")

            self.data = bytearray(data)

    def write(self, data: bytes, offset: int = 0):
        end = offset + len(data)

        if end > PAGE_SIZE:
            raise ValueError("Data exceeds page size")

        self.data[offset:end] = data

    def read(self, offset: int = 0, size: int = None) -> bytes:
        if size is None:
            size = PAGE_SIZE - offset

        end = offset + size

        if end > PAGE_SIZE:
            raise ValueError("Read exceeds page size")

        return bytes(self.data[offset:end])

    def raw(self) -> bytes:
        return bytes(self.data)

    
    def insert_row(self, row: Row, offset: int):

        row_data = row.serialize()

        row_size = len(row_data)

        record = (row_size.to_bytes(4, 'little') + row_data)

        self.write(record, offset)

        return len(record)


    def read_row(self, offset: int):

        row_size = int.from_bytes(
            self.read(offset, 4),
            'little'
        )
        
        row_data = self.read(offset + 4, row_size)

        return Row.deserialize(row_data)


        
