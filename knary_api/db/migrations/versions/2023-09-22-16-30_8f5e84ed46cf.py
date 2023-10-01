"""create user table

Revision ID: 8f5e84ed46cf
Revises: 2b7380507a71
Create Date: 2023-09-22 16:30:38.831822

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "8f5e84ed46cf"
down_revision = "2b7380507a71"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("email", sa.String(length=200), nullable=True),
        sa.Column("password", sa.String(length=200), nullable=True),
        sa.Column("hashed_password", sa.String(length=200), nullable=True),
        sa.Column("is_active", sa.Boolean, nullable=True, default=False),
        sa.Column("is_superuser", sa.Boolean, nullable=True, default=False),
        sa.Column("is_verified", sa.Boolean, nullable=True, default=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("user")
