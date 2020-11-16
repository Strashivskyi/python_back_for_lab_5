import doctest
from operator import attrgetter

from models import AbstractDish
from models.Condition import Condition
from models.GreekSalad import GreekSalad
from models.Muffin import Muffin
from models.MushroomSoup import MushroomSoup
from models.SortType import SortType


class RestorationManagerUtils:
    def __init(self):
        pass

    @staticmethod
    def sort_by_price(dishes: AbstractDish, sort_type: SortType):
        """
        returns sorted list
        >>> mushroom_soup = MushroomSoup(15.05, 45, 45, 'goul', 'tgggtgtgt', 'rrgggtg', Condition.Hot, 'gtgtgtg', 'rfrfrfrfrf')
        >>> muffin = Muffin(11.56, 33, 33, 'rgtg', 'frfrfr', 'rfrfrf', Condition.Hot, 11, 'vrvrvr')
        >>> greek_salad = GreekSalad(14.5, 78, 54, 'gggh', 'tgbtgtg', 'tgtgtg', Condition.Hot, 'gggg', 14)
        >>> dishes = [mushroom_soup, muffin, greek_salad]
        >>> names = []
        >>> for dish in RestorationManagerUtils.sort_by_price(dishes, SortType.Asc): names.append(str(dish))
        >>> print(str(names))
        ['muffin', 'greek_salad', 'mushroom_soup']
        >>> del names[:]
        >>> for dish in RestorationManagerUtils.sort_by_price(dishes, SortType.Desc): names.append(str(dish))
        >>> print(str(names))
        ['mushroom_soup', 'greek_salad', 'muffin']
        """
        if sort_type == SortType.Asc:
            return sorted(dishes, key=attrgetter('price_in_UAH'))
        else:
            return sorted(dishes, key=attrgetter('price_in_UAH'), reverse=True)


if __name__ == "__main__":
    doctest.testmod()
