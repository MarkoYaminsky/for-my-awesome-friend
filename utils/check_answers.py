import os


def check_answers(phrase_if_susccessful: str, **kwargs: tuple):
    for key, value in kwargs.items():
        storyline, correct_value, error_message = map(str.lstrip, value)
        env_variable = os.getenv(key.upper())

        if not env_variable:
            print(storyline)
            return

        if env_variable and (env_variable.lower() != correct_value.lower()):
            print(error_message)
            print(env_variable)
            return

    print(phrase_if_susccessful)
