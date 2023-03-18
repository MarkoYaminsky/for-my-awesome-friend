from utils.check_answers import check_answers
from utils.phase import phase
from utils.get_parts_of_file import get_parts_of_file


@phase
def development():
    boy_part, boy_error, body_part, body_error, pizza_part, pizza_error, finish = get_parts_of_file('development')

    check_answers(
        fourth_boy=(boy_part, 'Андрій', boy_error),
        painful_part=(body_part, 'Спина', body_error),
        pizza=(pizza_part, 'Палермо', pizza_error),
        phrase_if_susccessful=finish
    )
