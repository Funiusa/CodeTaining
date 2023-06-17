from typing import Union, Type


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


class Army:
    def __init__(self):
        self.units = []

    def get_warrior(self) -> Union[Warrior, Knight, None]:
        if len(self.units):
            unit = self.units.pop()
            return unit
        return None

    def add_units(self, unit: Type[Union[Warrior, Knight]], quantity: int) -> None:
        for i in range(quantity):
            self.units.append(unit())


class Battle:
    def fight(self, army1: Army, army2: Army) -> bool:
        warrior1 = army1.get_warrior()
        warrior2 = army2.get_warrior()
        while warrior1 and warrior2:
            if fight(warrior1, warrior2):
                warrior2 = army2.get_warrior()
            else:
                warrior1 = army1.get_warrior()
        return warrior1 is not None


def fight(warrior_1: Union[Warrior, Knight], warrior_2: Union[Warrior, Knight]) -> bool:
    while warrior_1.is_alive and warrior_2.is_alive:
        warrior_2.health -= warrior_1.attack
        warrior_1.health -= warrior_2.attack if warrior_1.is_alive else 0
    return warrior_1.is_alive


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # fight tests
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

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")

    army_1 = Army()
    army_2 = Army()
    army_1.add_units(Warrior, 10)
    army_2.add_units(Warrior, 11)
    battle = Battle()
    assert battle.fight(army_1, army_2) == True
