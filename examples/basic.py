from mydb.page import Page
from mydb.storage import Storage


storage = Storage("./data/mydb.db")


# Create a page
page = Page()

page.write(
    b"Hello MyDB!"
)


# Save page to disk
storage.write_page(
    0,
    page
)


# Read page from disk
loaded_page = storage.read_page(0)


print(
    loaded_page.read(
        0,
        11
    )
)


print(
    "Pages:",
    storage.page_count()
)


storage.close()