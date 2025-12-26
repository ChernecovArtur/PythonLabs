import json
from functools import reduce
from typing import Any, Callable


def load_json(path: str) -> Any:
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Ошибка загрузки файла {path}") from exc


def compose(*functions: Callable) -> Callable:
    
    return reduce(lambda f, g: lambda x: f(g(x)), functions)
