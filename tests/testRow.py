from mydb.row import Row


row = Row(
    row_id=1,
    name="Hasan",
    age=24
)

print("Original:")
print(row)


data = row.serialize()

print("\nSerialized:")
print(data)

print("\nSize:")
print(len(data))


new_row = Row.deserialize(data)

print("\nDeserialized:")
print(new_row)