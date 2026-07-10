from library_item import LibraryItem


class Book(LibraryItem):
    """A book in the library."""

    def __init__(self, item_id: int, title: str, author: str, year: int, genre: str):
        super().__init__(item_id, title, author, year)
        self._genre = genre

    @property
    def genre(self) -> str:
        return self._genre

    def get_description(self) -> str:
        return f"Book | {self.title} by {self.author} ({self.year}) - Genre: {self.genre}"
