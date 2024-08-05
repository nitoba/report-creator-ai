from typing import Generic, List, TypeVar

T = TypeVar('T')


class Paginated(Generic[T]):
    page: int
    size: int
    total: int
    data: List[T]

    def __init__(self, page: int, size: int, total: int, data: List[T]):
        self.page = page
        self.size = size
        self.total = total
        self.data = data
