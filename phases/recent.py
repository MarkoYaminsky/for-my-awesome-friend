from utils.check_answers import check_answers
from utils.get_parts_of_file import get_parts_of_file
from utils.phase import phase


@phase
def recent():
    subject_part, subject_error, friend_part, friend_error, date_part, date_error, finish = get_parts_of_file('recent')

    check_answers(
        highest_subject=(subject_part, 'Командна робота', subject_error),
        dear_friend=(friend_part, 'Настя', friend_error),
        unpacking_date=(date_part, '15 березня', date_error),
        phrase_if_susccessful=finish
    )
