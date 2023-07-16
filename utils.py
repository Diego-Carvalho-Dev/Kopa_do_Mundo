
from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError

def data_processing(selection_info):
    titles = int(selection_info.get('titles', 0))
    first_cup = int(selection_info.get('first_cup', '0').split('-')[0])



    if titles < 0:
        raise NegativeTitlesError()

    if first_cup < 1930 or (first_cup - 1930) % 4 != 0:
        raise InvalidYearCupError()

    max_possible_titles = (2023 - first_cup) // 4 + 1
    if titles > max_possible_titles:
        raise ImpossibleTitlesError()


