import struct


class Row:
    def __init__(self, row_id: int, name: str, age: int):
        self.row_id = row_id
        self.name = name
        self.age = age

    def serialize(self) -> bytes:
        name_bytes = self.name.encode('utf-8')

        data = struct.pack(
            "<iiI",
            self.row_id,
            self.age,
            len(name_bytes),
        )

        return data + name_bytes

    
    @classmethod
    def deserialize(cls, data: bytes):
        row_id, age, name_length = struct.unpack(
            "<iiI",
            data[:12]
        )

        name_bytes = data[12 : 12 + name_length]
        name = name_bytes.decode('utf-8')

        return cls(row_id, name, age)

    
    def __repr__(self):
        return (
            f"Row(id={self.row_id}, "
            f"name='{self.name}', "
            f"age={self.age})"
        )


    
        