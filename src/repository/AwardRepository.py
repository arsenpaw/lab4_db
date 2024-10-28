from src.context.dbcontext import Award
from src.repository.BaseRepository import Repository


class AwardRepository(Repository):
    def __init__(self):
        super().__init__(Award)

