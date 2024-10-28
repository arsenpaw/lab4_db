from src.context.dbcontext import Award
from src.services.BaseService import BaseService



class AwardService(BaseService):
    def __init__(self):
        super().__init__(Award)