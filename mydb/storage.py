from pathlib import Path

from .page import PAGE_SIZE, Page


class Storage:
    def __init__(self, path: str):
        self.path = Path(path)

        self.path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self.file = open(
            self.path,
            "a+b"
        )

    def page_count(self) -> int:
        self.file.seek(0, 2)

        size = self.file.tell()

        return size // PAGE_SIZE

    def write_page(self, page_id: int, page: Page):
        offset = page_id * PAGE_SIZE

        self.file.seek(offset)

        self.file.write(page.raw())

        self.file.flush()

    def read_page(self, page_id: int) -> Page:
        offset = page_id * PAGE_SIZE

        self.file.seek(offset)

        data = self.file.read(PAGE_SIZE)

        if len(data) != PAGE_SIZE:
            raise ValueError(
                f"Page {page_id} does not exist"
            )

        return Page(data)

    def close(self):
        self.file.close()