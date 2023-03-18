from utils.get_parts_of_file import get_parts_of_file
from utils.check_answers import check_answers
from utils.phase import phase


@phase
def intro():
    start, name_error, animal_part, animal_error, finish = get_parts_of_file('intro')

    check_answers(
        name=(start, 'Ліа', name_error),
        animal=(animal_part, 'Видра', animal_error),
        phrase_if_susccessful=finish
    )
