cube3d = {
    "vertexes": [
        [0, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 0, 0, 1], [0, 1, 0, 0, 1],
        [0, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 1, 1, 0, 1], [0, 1, 1, 0, 1],
    ],
    "faces": (
        (0, 1, 2, 3), (4, 5, 6, 7), (0, 1, 5, 4),
        (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7),
    )
}


cube4d = {
    "vertexes": [
        [0, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 0, 0, 1], [0, 1, 0, 0, 1],
        [0, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 1, 1, 0, 1], [0, 1, 1, 0, 1],
        [0, 0, 0, 1, 1], [1, 0, 0, 1, 1], [1, 1, 0, 1, 1], [0, 1, 0, 1, 1],
        [0, 0, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [0, 1, 1, 1, 1],
    ],
    "faces": (
        (0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11), (12, 13, 14, 15),
        (0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7),
        (4, 5, 13, 12), (5, 6, 14, 13), (6, 7, 15, 14), (7, 4, 12, 15),
        (8, 9, 13, 12), (9, 10, 14, 13), (10, 11, 15, 14), (11, 8, 12, 15),
        (8, 9, 1, 0), (9, 10, 2, 1), (10, 11, 3, 2), (11, 8, 0, 3),
    )
}