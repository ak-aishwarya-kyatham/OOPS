from media_item import MediaItem
from movie import Movie
from series import Series


class MediaStore:
    """MediaStore manages media items with encapsulated operations."""

    def __init__(self):
        self._items: list[MediaItem] = []

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


def create_demo_store() -> MediaStore:
    media_store = MediaStore()
    media_store.add_item(Movie(1, "The Last Horizon", "S. Walker", 2024, "Science Fiction"))
    media_store.add_item(Movie(2, "Ocean of Algorithms", "N. Patel", 2023, "Technology"))
    media_store.add_item(Series(3, "Creative Coding", "A. Summers", 2025, 2))
    media_store.add_item(Series(4, "Planet Earth Explorer", "C. Rivera", 2024, 1))
    return media_store
