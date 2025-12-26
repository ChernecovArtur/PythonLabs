import os
import re
from dataclasses import dataclass
from typing import Any

import requests


WIKI_API_URL: str = "https://ru.wikipedia.org/w/api.php"
OUT_DIR: str = "./data/wiki"

HEADERS: dict[str, str] = {
    "User-Agent": "PermianRAGLab/0.1 (student project; contact: chernecov_artur@mail.ru)",
}


TITLES: list[str] = [
    "Пермский период",
    "Палеозой",
    "Массовое пермское вымирание",
    "Сибирские траппы",
    "Терапсиды",
    "Пангея",
    "Триасовый период",
]


@dataclass
class ArticleStats:
    title: str
    chars: int
    words: int


def normalize_filename(title: str) -> str:
    safe: str = re.sub(r"[^0-9A-Za-zА-Яа-яЁё_\- ]+", "", title).strip()
    safe = safe.replace(" ", "_")
    return f"{safe}.txt"


def fetch_wikipedia_plaintext(title: str) -> str:
    params: dict[str, Any] = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "explaintext": 1,
        "redirects": 1,
        "titles": title,
        "maxlag": 5,
    }

    response = requests.get(
        WIKI_API_URL,
        params=params,
        headers=HEADERS,
        timeout=30,
    )
    response.raise_for_status()

    data: dict[str, Any] = response.json()
    pages: dict[str, Any] = data.get("query", {}).get("pages", {})
    if not pages:
        return ""

    page: dict[str, Any] = next(iter(pages.values()))
    extract: str = page.get("extract", "")
    return extract


def count_words(text: str) -> int:
    tokens: list[str] = re.findall(r"[A-Za-zА-Яа-яЁё0-9]+", text)
    return len(tokens)


def save_text(path: str, text: str) -> None:
    with open(path, "w", encoding="utf-8") as file:
        file.write(text)


def print_dataset_stats(stats: list[ArticleStats]) -> None:
    total_docs: int = len(stats)
    total_chars: int = sum(s.chars for s in stats)
    total_words: int = sum(s.words for s in stats)

    avg_chars: float = total_chars / total_docs if total_docs else 0.0
    avg_words: float = total_words / total_docs if total_docs else 0.0

    print("\n=== Dataset stats ===")
    print(f"Documents: {total_docs}")
    print(f"Total chars: {total_chars}")
    print(f"Total words: {total_words}")
    print(f"Avg chars/doc: {avg_chars:.1f}")
    print(f"Avg words/doc: {avg_words:.1f}")

    longest: ArticleStats = max(stats, key=lambda s: s.words)
    shortest: ArticleStats = min(stats, key=lambda s: s.words)
    print(f"Longest (words): {longest.title} -> {longest.words}")
    print(f"Shortest (words): {shortest.title} -> {shortest.words}")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)

    stats: list[ArticleStats] = []

    for title in TITLES:
        text: str = fetch_wikipedia_plaintext(title)
        if not text.strip():
            print(f"Skip (empty): {title}")
            continue

        filename: str = normalize_filename(title)
        path: str = os.path.join(OUT_DIR, filename)
        save_text(path, text)

        chars: int = len(text)
        words: int = count_words(text)
        stats.append(ArticleStats(title=title, chars=chars, words=words))
        print(f"Saved: {title} -> {path} ({words} words)")

    if stats:
        print_dataset_stats(stats)
    else:
        print("No articles downloaded.")


if __name__ == "__main__":
    main()
