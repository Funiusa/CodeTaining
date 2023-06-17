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


class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.attack = 4
        self.vampirism = 50


class Army:
    def __init__(self):
        self.units = []

    def get_warrior(self) -> Union[Warrior, Knight, Defender, None]:
        if len(self.units):
            unit = self.units.pop()
            return unit
        return None

    def add_units(
            self,
            unit: Type[Union[Warrior, Knight, Defender, Vampire]],
            quantity: int
    ) -> None:
        self.units += [unit() for _ in range(quantity)]


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
        warrior_1: Union[Warrior, Knight, Defender, Vampire],
        warrior_2: Union[Warrior, Knight, Defender, Vampire]
) -> bool:
    defence_w1 = defence_w2 = 0
    if isinstance(warrior_1, Defender):
        defence_w1 = warrior_1.defence
    if isinstance(warrior_2, Defender):
        defence_w2 = warrior_2.defence
    while warrior_1.is_alive and warrior_2.is_alive:

        attack = warrior_1.attack - defence_w2
        if isinstance(warrior_1, Vampire):
            warrior_1.health += attack * warrior_1.vampirism // 100
        warrior_2.health -= max(attack, 0)
        if not warrior_2.is_alive:
            break

        attack = warrior_2.attack - defence_w1
        if isinstance(warrior_2, Vampire):
            warrior_2.health += attack * warrior_2.vampirism // 100
        warrior_1.health -= max(attack, 0)
        if not warrior_1.is_alive:
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
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()

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
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 4)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
