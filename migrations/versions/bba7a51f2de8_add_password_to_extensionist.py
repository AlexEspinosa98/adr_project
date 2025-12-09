"""add password column to user_extensionist

Revision ID: bba7a51f2de8
Revises: 3646f39f31c1
Create Date: 2025-11-28 00:00:00.000000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "bba7a51f2de8"
down_revision: Union[str, Sequence[str], None] = "3646f39f31c1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Add password column to user_extensionist."""
    op.add_column(
        "user_extensionist",
        sa.Column("password", sa.String(length=255), nullable=True),
    )


def downgrade() -> None:
    """Remove password column from user_extensionist."""
    op.drop_column("user_extensionist", "password")

