from typing import Union, Type


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.is_alive = True


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


class Rookie(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 1


class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 3
        self.defence = 2


class Army:
    def __init__(self):
        self.units = []

    def get_warrior(self) -> Union[Warrior, Knight, Defender, None]:
        if len(self.units):
            unit = self.units.pop()
            return unit
        return None

    def add_units(
            self, unit: Type[Union[Warrior, Knight, Defender]], quantity: int) -> None:
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


def fight(
        warrior_1: Union[Warrior, Knight, Defender],
        warrior_2: Union[Warrior, Knight, Defender]
) -> bool:
    defence_w1 = defence_w2 = 0
    if isinstance(warrior_1, Defender):
        defence_w1 = warrior_1.defence
    if isinstance(warrior_2, Defender):
        defence_w2 = warrior_2.defence
    while warrior_1.is_alive and warrior_2.is_alive:

        attack = warrior_1.attack - defence_w2
        warrior_2.health -= max(attack, 0)
        if warrior_2.health <= 0:
            warrior_2.is_alive = False
            break

        attack = warrior_2.attack - defence_w1
        warrior_1.health -= max(attack, 0)
        if warrior_1.health <= 0:
            warrior_1.is_alive = False
            break

    return warrior_1.is_alive


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
    army_1 = Army()
    army_2 = Army()
    army_1.add_units(Defender, 2)
    army_1.add_units(Warrior, 1)
    army_1.add_units(Defender, 1)
    army_2.add_units(Warrior, 5)
    battle = Battle()
    assert battle.fight(army_1, army_2) == False
    unit_1 = Defender()
    unit_2 = Rookie()
    fight(unit_1, unit_2)
    print(unit_1.health)
