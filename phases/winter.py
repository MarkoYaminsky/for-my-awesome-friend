from utils.check_answers import check_answers
from utils.phase import phase
from utils.get_parts_of_file import get_parts_of_file


@phase
def winter():
    discord_part, discord_error, lesson_part, lesson_error, food_part, food_error, \
    music_part, music_error, singer_part, singer_error, finish = get_parts_of_file('winter')

    check_answers(
        discord_name=(discord_part, 'Видроksf', discord_error),
        first_lesson=(lesson_part, 'Console', lesson_error),
        traditional_food=(food_part, 'Кебаб', food_error),
        music_game=(music_part, 'Геншин', music_error),
        interesting_singer=(singer_part, 'Fakasutra', singer_error),
        phrase_if_susccessful=finish
    )
