import abc


class LibraryItem(abc.ABC):
    """Abstract base class representing a library item."""

    def __init__(self, item_id: int, title: str, author: str, year: int):
        self._item_id = item_id
        self._title = title
        self._author = author
        self._year = year
        self._available = True

    @property
    def item_id(self) -> int:
        return self._item_id

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def year(self) -> int:
        return self._year

    @property
    def available(self) -> bool:
        return self._available

    def borrow(self) -> bool:
        if self._available:
            self._available = False
            return True
        return False

    def return_item(self) -> None:
        self._available = True

    def matches_title(self, search_term: str) -> bool:
        return search_term.lower() in self._title.lower()

    @abc.abstractmethod
    def get_description(self) -> str:
        pass
