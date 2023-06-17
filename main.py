import argparse

from Space.engine import Engine
from Space.objects import Object4D
from Space.constants import WIDTH, HEIGHT
from Space import shapes


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", type=int, default=WIDTH)
    parser.add_argument("--height", type=int, default=HEIGHT)
    parser.add_argument("--shape", type=str, choices=[obj for obj in shapes.__dict__.keys() if "__" not in obj])

    args = parser.parse_args()

    engine = Engine(args.width, args.height)
    engine.objects = [
        Object4D(engine, args.shape)
    ]

    engine.run()
