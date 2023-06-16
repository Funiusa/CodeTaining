class Warrior:
    def __init__(self):
        self._health = 50
        self._attack = 5
        self._is_alive = True

    @property
    def health(self):
        return self._health

    @property
    def attack(self):
        return self._attack

    @property
    def is_alive(self):
        return self._is_alive

    def enemy_attack(self, damage: int) -> bool:
        self._health -= damage
        if self._health <= 0:
            self._is_alive = False
        return self._is_alive


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self._attack = 7


def fight(unit_1, unit_2) -> bool:
    while True:
        if unit_2.enemy_attack(unit_1.attack) <= 0:
            return True
        if unit_1.enemy_attack(unit_2.attack) <= 0:
            return False


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")
