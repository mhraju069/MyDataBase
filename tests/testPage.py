from mydb.page import Page

page = Page()

page.write(b"Hello MyDB")

print(page.read()[:10])