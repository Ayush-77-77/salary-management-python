# Import every model here so that importing `employee_salary_api.models`
# registers all tables on Base.metadata (Alembic relies on this).
from employee_salary_api.models.department import Department

__all__ = ["Department"]
