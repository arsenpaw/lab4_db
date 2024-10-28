from src.repository.BaseRepository import Repository
from utils.utils import Award


class AwardRepository(Repository):
    def __init__(self):
        super().__init__(Award)

