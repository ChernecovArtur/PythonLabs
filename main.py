from task1_countries import (
    filter_countries,
    nordic_reduce,
    to_upper,
)
from task2_aco import ant_colony_optimization, generate_points
from utils import load_json


def main():
    print("=== ЗАДАНИЕ 1: СТРАНЫ ===")
    countries = load_json("countries.json")

    print("Верхний регистр:")
    print(to_upper(countries))

    print("\nФильтрация:")
    print(filter_countries(countries))

    print("\nСеверная Европа:")
    print(nordic_reduce())

    print("\n=== ЗАДАНИЕ 2: МУРАВЬИНЫЙ АЛГОРИТМ ===")
    points = list(generate_points(200))
    optimizer = ant_colony_optimization(points, iterations=10)

    for path, length in optimizer:
        print(f"Длина маршрута: {length:.2f}")


if __name__ == "__main__":
    main()
