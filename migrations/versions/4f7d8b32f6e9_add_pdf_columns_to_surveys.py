"""add pdf columns to survey tables

Revision ID: 4f7d8b32f6e9
Revises: bba7a51f2de8
Create Date: 2025-11-28 00:00:00.000000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4f7d8b32f6e9"
down_revision: Union[str, Sequence[str], None] = "bba7a51f2de8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Add file_pdf columns to all survey tables."""
    op.add_column(
        "survey_1",
        sa.Column("file_pdf", sa.String(length=255), nullable=True),
    )
    op.add_column(
        "survey_2",
        sa.Column("file_pdf", sa.String(length=255), nullable=True),
    )
    op.add_column(
        "survey_3",
        sa.Column("file_pdf", sa.String(length=255), nullable=True),
    )


def downgrade() -> None:
    """Remove file_pdf columns from survey tables."""
    op.drop_column("survey_1", "file_pdf")
    op.drop_column("survey_2", "file_pdf")
    op.drop_column("survey_3", "file_pdf")

