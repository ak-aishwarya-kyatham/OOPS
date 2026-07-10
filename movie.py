from media_item import MediaItem


class Movie(MediaItem):
    """A movie in the media store."""

    def __init__(self, item_id: int, title: str, director: str, year: int, genre: str):
        super().__init__(item_id, title, director, year)
        self._genre = genre

    @property
    def genre(self) -> str:
        return self._genre

    def get_description(self) -> str:
        return f"Movie | {self.title} directed by {self.author} ({self.year}) - Genre: {self.genre}"
