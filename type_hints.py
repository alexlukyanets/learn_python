from typing import Optional, Any, Union, List, Tuple, Dict, Iterable


class Charackter:

    def __init__(self, armor: int, power: int):
        self.power = power
        self.armor = armor
        self.health = 100

    def hit(self, damage: int):
        self.health -= damage

    def is_alive(self):
        return self.health > 0


c1 = Charackter(10, 20)
c1.hit(20)

armour: int
armour = None

price: Optional[int]
price: 10
price: None
price: 'sdsadsa'

attrack: Any = 1
attrack = 'hi'

lenght: Union[int, float]
lenght = 1
lenght = 1.2
lenght = '123'

quotes: list
quotes = 'Just'

quotes: List[int]
quotes: List[int]  # Set, Frozenset

player: Tuple[str, int] = ("Krnjik", 2750)

changes_in: Tuple[int: ...]
changes_in = (1, 2, 3, 4, 5, 6)
changes_in = (1, "abcedf")

cheess_player: Dict[str, int]