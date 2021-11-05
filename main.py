from game import Game


def test1():
    predator, prey = Game.generate_creatures()

    while prey.do_move() or predator.do_move():
        print(f"Prey: {prey.position}\nPredator: {predator.position}\n")


def test2():
    Game.hunt(*Game.generate_creatures())


if __name__ == "__main__":
    test1()
    test2()

# TODO: replace with normal tests
