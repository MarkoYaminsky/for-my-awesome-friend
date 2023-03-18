from utils.check_answers import check_answers
from utils.get_parts_of_file import get_parts_of_file
from utils.phase import phase


@phase
def epilogue():
    secret_key, key_error, secret_ending = get_parts_of_file('epilogue')

    check_answers(
        secret_code=(secret_key, 'Ми тебе любимо', key_error),
        phrase_if_susccessful=secret_ending
    )
