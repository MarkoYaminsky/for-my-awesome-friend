from dotenv import load_dotenv
from os import getenv

from phases.acquaintance import acquaintance
from phases.development import development
from phases.epilogue import epilogue
from phases.intro import intro
from phases.recent import recent
from phases.winter import winter

load_dotenv()
if __name__ == '__main__':
    phase = getenv('COMPLETION_PHASE')

    intro()
    acquaintance()
    development()
    winter()
    recent()
    epilogue()
