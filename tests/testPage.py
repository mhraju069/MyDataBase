from mydb.page import Page
from mydb.row import Row
from mydb.storage import Storage


storage = Storage("./data/mydb.db")

page = Page()

row = Row(
    row_id=1,
    name="Hasan",
    age=24
)

page.insert_row(row, offset=0)

storage.write_page(
    page_id=0,
    page=page
)

loaded_page = storage.read_page(0)

loaded_row = loaded_page.read_row(0)

print(loaded_row)

storage.close()