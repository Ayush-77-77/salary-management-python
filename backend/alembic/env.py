from logging.config import fileConfig

from sqlalchemy import create_engine, pool

from alembic import context
from employee_salary_api import models  # noqa: F401  (import registers all tables on Base.metadata)
from employee_salary_api.core.config import get_settings
from employee_salary_api.db.base import Base

# Alembic's config object (reads [tool.alembic] in pyproject.toml + alembic.ini).
config = context.config

# Set up Python logging from the [loggers]/[handlers] sections of alembic.ini.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# The tables Alembic compares against the real database for --autogenerate.
target_metadata = Base.metadata

# Same connection details the app uses, from .env, never hardcoded.
database_url = get_settings().database_url


def run_migrations_offline() -> None:
    """Generate SQL scripts without connecting to the database (`alembic upgrade head --sql`)."""
    context.configure(
        url=database_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Connect to the database and apply migrations (the normal mode)."""
    engine = create_engine(database_url, poolclass=pool.NullPool)

    with engine.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
