"""add default to is_active in actions_log

Revision ID: 9d0f51dc1dc7
Revises: 973c3ffd885a
Create Date: 2025-10-27 15:13:26.113569

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9d0f51dc1dc7"
down_revision: Union[str, Sequence[str], None] = "fafeeb74ccc1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        "actions_log",
        "is_active",
        server_default=sa.text("true"),
        existing_type=sa.Boolean(),
        nullable=False,
    )
    op.alter_column(
        "actions_log",
        "created_at",
        server_default=sa.func.now(),
        existing_type=sa.DateTime(),
        nullable=False,
    )
    op.alter_column(
        "actions_log",
        "updated_at",
        server_default=sa.func.now(),
        existing_type=sa.DateTime(),
        nullable=False,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        "actions_log",
        "is_active",
        server_default=None,
        existing_type=sa.Boolean(),
        nullable=True,
    )
    op.alter_column(
        "actions_log",
        "created_at",
        server_default=None,
        existing_type=sa.DateTime(),
        nullable=True,
    )
    op.alter_column(
        "actions_log",
        "updated_at",
        server_default=None,
        existing_type=sa.DateTime(),
        nullable=True,
    )
