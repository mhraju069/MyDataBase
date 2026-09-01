from mydb.page import Page
from mydb.row import Row


page = Page()


row = Row(
    row_id=1,
    name="Hasan",
    age=24
)


page.insert_row(
    row,
    offset=0
)


loaded_row = page.read_row(0)


print(loaded_row)