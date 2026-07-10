from library_item import LibraryItem


class Magazine(LibraryItem):
    """A magazine issue in the library."""

    def __init__(self, item_id: int, title: str, author: str, year: int, issue_number: int):
        super().__init__(item_id, title, author, year)
        self._issue_number = issue_number

    @property
    def issue_number(self) -> int:
        return self._issue_number

    def get_description(self) -> str:
        return f"Magazine | {self.title} by {self.author} ({self.year}) - Issue #{self.issue_number}"
