from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from employee_salary_api.db.base import Base, TimestampMixin


class Department(TimestampMixin, Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)

    def __repr__(self) -> str:
        return f"Department(id={self.id!r}, name={self.name!r})"
