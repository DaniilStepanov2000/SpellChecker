import json
from dataclasses import dataclass
import pathlib


@dataclass
class Settings:
    """Class for storing settings.

    Args:
        BASE_number_articles: The number of articles to be parsed.
        BASE_start_URL: Initial URL.
    """
    BASE_number_articles: int
    BASE_start_URL: str

    @classmethod
    def from_json(cls, file_path: pathlib.Path):
        with file_path.open('r') as file:
            our_config = json.load(file)

        return cls(
            BASE_number_articles=our_config.get('BASE_number_articles', ''),
            BASE_start_URL=our_config.get('BASE_start_URL', '')
        )
