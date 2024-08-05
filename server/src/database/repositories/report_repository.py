from src.database.connection import get_db
from src.database.models import ReportModel
from src.database.paginated import Paginated


class ReportRepository:
    def save(self, report: ReportModel) -> None:
        with get_db() as db:
            db.add(report)
            db.commit()
            # refresh the instance to get the id
            db.refresh(report)

    def find_all_by_user_id(
        self, user_id: str, page_index: int = 0, page_size: int = 10
    ) -> Paginated[ReportModel]:
        with get_db() as db:
            total = db.query(ReportModel).filter_by(user_id=user_id).count()
            reports = (
                db.query(ReportModel)
                .filter_by(user_id=user_id)
                .order_by(ReportModel.created_at.desc())
                .offset(page_index * page_size)
                .limit(page_size)
                .all()
            )

            return Paginated(
                page=page_index,
                size=page_size,
                total=total,
                data=reports,
            )

    def find_by_id(self, report_id: str) -> ReportModel | None:
        with get_db() as db:
            return db.query(ReportModel).filter_by(id=report_id).first()

    def find_by_user_id(self, user_id: str) -> ReportModel | None:
        with get_db() as db:
            return db.query(ReportModel).filter_by(user_id=user_id).first()

    def find_by_user_id_and_report_id(
        self, user_id: str, report_id: str
    ) -> ReportModel | None:
        with get_db() as db:
            return db.query(ReportModel).filter_by(user_id=user_id, id=report_id).first()
