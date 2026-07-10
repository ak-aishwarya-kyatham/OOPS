from media_item import MediaItem


class Series(MediaItem):
    """A TV series in the media store."""

    def __init__(self, item_id: int, title: str, creator: str, year: int, season_number: int):
        super().__init__(item_id, title, creator, year)
        self._season_number = season_number

    @property
    def season_number(self) -> int:
        return self._season_number

    def get_description(self) -> str:
        return f"Series | {self.title} by {self.author} ({self.year}) - Season {self.season_number}"
