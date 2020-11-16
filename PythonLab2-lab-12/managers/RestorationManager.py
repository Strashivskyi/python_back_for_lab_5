import doctest

from models import AbstractDish
from models.Condition import Condition
from models.GreekSalad import GreekSalad
from models.Muffin import Muffin
from models.MushroomSoup import MushroomSoup


class RestorationManager:
    def __init(self):
        pass

    def find_by_condition(self, dishes: AbstractDish, certain_condition: Condition):
        """
        returns list of objects by condition
        >>> mushroom_soup = MushroomSoup(15.05, 45, 45, 'goul', 'tgggtgtgt', 'rrgggtg', Condition.Hot, 'gtgtgtg', 'rfrfrfrfrf')
        >>> muffin = Muffin(11.56, 33, 33, 'rgtg', 'frfrfr', 'rfrfrf', Condition.Hot, 11, 'vrvrvr')
        >>> greek_salad = GreekSalad(14.5, 78, 54, 'gggh', 'tgbtgtg', 'tgtgtg', Condition.Cold, 'gggg', 14)
        >>> dishes = [mushroom_soup, muffin, greek_salad]
        >>> restorationManager = RestorationManager()
        >>> names = []
        >>> for dish in restorationManager.find_by_condition(dishes, Condition.Hot): names.append(str(dish))
        >>> print(str(names))
        ['mushroom_soup', 'muffin']
        """

        found_dishes = []
        for dish in dishes:
            if dish.condition == certain_condition:
                found_dishes.append(dish)
        return found_dishes


if __name__ == "__main__":
    doctest.testmod()
