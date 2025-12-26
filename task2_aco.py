import asyncio
import math
import random
from functools import partial
from typing import Dict, Generator, List, Tuple

import matplotlib.pyplot as plt

Point = Tuple[float, float, float]
Edge = Tuple[int, int, float]


def generate_points(
    n: int,
    bounds: tuple = (0, 100),
) -> Generator[Point, None, None]:

    for _ in range(n):
        yield tuple(random.uniform(*bounds) for _ in range(3))


def euclidean(p1: Point, p2: Point) -> float:
 
    return math.dist(p1, p2)


def generate_roads(
    points: List[Point],
    bidirectional_ratio: float = 0.7,
) -> Generator[Edge, None, None]:
 
    for i, p1 in enumerate(points):
        for j, p2 in enumerate(points):
            if i != j and random.random() < bidirectional_ratio:
                yield i, j, euclidean(p1, p2)


def initialize_pheromones(points: List[Point]) -> Dict[tuple, float]:

    return {
        (i, j): 1.0
        for i in range(len(points))
        for j in range(len(points))
        if i != j
    }


def transition_probability(
    pheromone: float,
    distance: float,
    alpha: float = 1.0,
    beta: float = 2.0,
) -> float:
    return (pheromone ** alpha) * ((1 / distance) ** beta)


def evaporate(
    pheromones: Dict[tuple, float],
    rate: float = 0.5,
) -> Dict[tuple, float]:

    return {k: v * (1 - rate) for k, v in pheromones.items()}


def calculate_path_length(path: List[Edge]) -> float:

    return sum(edge[2] for edge in path)


def update_pheromones(
    pheromones: Dict[tuple, float],
    path: List[Edge],
    q: float = 100.0,
) -> Dict[tuple, float]:

    length = calculate_path_length(path)
    return {
        k: v + (q / length if k in [(a, b) for a, b, _ in path] else 0)
        for k, v in pheromones.items()
    }


def construct_path(
    pheromones: Dict[tuple, float],
    points: List[Point],
) -> List[Edge]:

    visited = set()
    path = []
    current = 0

    while len(visited) < len(points) - 1:
        visited.add(current)
        candidates = filter(
            lambda x: x not in visited,
            range(len(points)),
        )
        next_city = min(
            candidates,
            key=lambda j: pheromones.get((current, j), 1),
        )
        distance = euclidean(points[current], points[next_city])
        path.append((current, next_city, distance))
        current = next_city

    return path


def ant_colony_optimization(
    points: List[Point],
    iterations: int = 50,
):

    pheromones = initialize_pheromones(points)

    for _ in range(iterations):
        paths = (
            construct_path(pheromones, points)
            for _ in range(len(points))
        )
        best_path = min(paths, key=calculate_path_length)
        pheromones = evaporate(
            update_pheromones(pheromones, best_path)
        )
        yield best_path, calculate_path_length(best_path)


async def visualize_optimization(generator):

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")

    async for path, length in generator:
        ax.clear()
        ax.set_title(f"Лучший путь: {length:.2f}")
        await asyncio.sleep(0.1)
