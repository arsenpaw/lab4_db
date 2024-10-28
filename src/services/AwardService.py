from src.repository.AwardRepository import AwardRepository
from src.services.BaseService import BaseService
from utils.utils import Award


class AwardService(BaseService):
    def __init__(self):
        super().__init__(Award)