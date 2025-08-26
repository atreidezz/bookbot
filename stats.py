from collections import Counter


def get_num_words(book_contents: str) -> int:
    return len(book_contents.split())


def get_chars_count(book_contents: str) -> dict[str, int]:
    return dict(Counter(book_contents.lower()))


def sorted_dictionaries(chars_counts: dict[str, int]) -> list[dict[str, int]]:
    return [
        {"char": k, "num": v}
        for k, v in chars_counts.items()
        if k.isalpha()
    ]
