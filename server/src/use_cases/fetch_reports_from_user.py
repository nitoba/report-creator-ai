from src.database.repositories.report_repository import ReportRepository


class FetchReportsFromUserUseCase:
    def __init__(self, report_repository: ReportRepository):
        self.report_repository = report_repository

    def execute(self, user_id: int):
        return self.report_repository.find_all_by_user_id(user_id)
