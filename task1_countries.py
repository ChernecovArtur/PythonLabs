from functools import reduce
from typing import Callable, List

from utils import load_json

COUNTRIES_PATH = "countries.json"
COUNTRIES_DATA_PATH = "countries-data.json"


def to_upper(countries: List[str]) -> List[str]:

    return list(map(str.upper, countries))


def filter_countries(countries: List[str]) -> dict:

    return {
        "contains_land": list(
            filter(lambda c: "land" in c.lower(), countries)
        ),
        "length_6": list(filter(lambda c: len(c) == 6, countries)),
        "length_ge_6": list(filter(lambda c: len(c) >= 6, countries)),
        "starts_with_e": list(filter(lambda c: c.startswith("E"), countries)),
    }


def nordic_reduce() -> str:
    """Объединение стран Северной Европы через reduce."""
    nordic = ["Финляндия", "Швеция", "Дания", "Норвегия", "Исландия"]
    result = reduce(lambda a, b: f"{a}, {b}", nordic)
    return f"{result} являются странами Северной Европы"


def manual_upper(countries: List[str]) -> List[str]:

    return [country.upper() for country in countries]


categorize_curried = (
    lambda pattern: lambda countries:
    [c for c in countries if pattern in c.lower()]
)


def categorize_closure(pattern: str) -> Callable:

    def inner(countries: List[str]) -> List[str]:
        return [c for c in countries if pattern in c.lower()]

    return inner


def sort_countries(data: list, key: str) -> list:

    return sorted(data, key=lambda c: c.get(key, ""))


def most_spoken_languages(data: list, top: int = 10) -> list:
 
    languages = reduce(
        lambda acc, c: acc + c.get("languages", []),
        data,
        [],
    )

    stats = {lang: languages.count(lang) for lang in set(languages)}
    return sorted(stats.items(), key=lambda x: x[1], reverse=True)[:top]


def most_populated(data: list, top: int = 10) -> list:

    return sorted(
        data,
        key=lambda c: c.get("population", 0),
        reverse=True,
    )[:top]


if __name__ == "__main__":
    countries = load_json(COUNTRIES_PATH)
    countries_data = load_json(COUNTRIES_DATA_PATH)

    print(to_upper(countries))
    print(filter_countries(countries))
    print(nordic_reduce())

    land_filter = categorize_curried("land")
    print(land_filter(countries))
