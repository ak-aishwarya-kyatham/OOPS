from library_item import LibraryItem
from book import Book
from magazine import Magazine


class Library:
    """Library manages library items with encapsulated operations."""

    def __init__(self):
        self._items: list[LibraryItem] = []

    def add_item(self, item: LibraryItem) -> None:
        self._items.append(item)

    def list_available_items(self) -> list[LibraryItem]:
        return [item for item in self._items if item.available]

    def find_item_by_title(self, search_term: str) -> list[LibraryItem]:
        return [item for item in self._items if item.matches_title(search_term)]

    def borrow_item(self, item_id: int) -> bool:
        for item in self._items:
            if item.item_id == item_id and item.available:
                return item.borrow()
        return False

    def return_item(self, item_id: int) -> bool:
        for item in self._items:
            if item.item_id == item_id and not item.available:
                item.return_item()
                return True
        return False


def create_demo_library() -> Library:
    library = Library()
    library.add_item(Book(1, "The Time Traveler's Notebook", "S. Walker", 2024, "Science Fiction"))
    library.add_item(Book(2, "Ocean of Algorithms", "N. Patel", 2023, "Technology"))
    library.add_item(Magazine(3, "Creative Coding Monthly", "A. Summers", 2025, 12))
    library.add_item(Magazine(4, "Planet Earth Explorer", "C. Rivera", 2024, 7))
    return library
