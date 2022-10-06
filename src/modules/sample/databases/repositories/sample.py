from typing import Tuple, List, Any
from src.databases.repo_base import CRUD

from ..models import SampleSchema
from ..interface import ISampleRepository


class SampleRepository(ISampleRepository, CRUD[SampleSchema]):
    def __init__(self, session):
        self.session = session
        self.model = SampleSchema

    def get_full_sample(
        self, page: int = None, page_size: int = None,
        **conditions: Any,
    ) -> Tuple[int, int, List[SampleSchema]]:
        pass
