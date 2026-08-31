from mydb.storage import Storage


storage = Storage("./data")

storage.write(
    "test.db",
    b"Hello MyDB"
)

data = storage.read("test.db")

print(data)