import os


def phase(function):
    def wrapper():
        if os.getenv('COMPLETION_PHASE').lower() != function.__name__:
            return
        function()

    return wrapper
