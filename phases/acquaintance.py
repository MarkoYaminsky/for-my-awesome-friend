from utils.get_parts_of_file import get_parts_of_file
from utils.check_answers import check_answers
from utils.phase import phase


@phase
def acquaintance():
    verb_part, verb_error, album_part, album_error, song_part, song_error, finish = get_parts_of_file('acquaintance')

    check_answers(
        prohibited_verb=(verb_part, 'кусати', verb_error),
        album_name=(album_part, 'ROSA', album_error),
        boombox_song=(song_part, 'Happy End', song_error),
        phrase_if_susccessful=finish
    )
