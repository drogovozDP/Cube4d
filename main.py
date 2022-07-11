from Space.engine import Engine
from Space.objects import Object4D


if __name__ == '__main__':
    engine = Engine()
    engine.objects = [
        Object4D(engine, "cube4d")
    ]

    engine.run()
