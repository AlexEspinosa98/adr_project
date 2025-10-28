"""add initial actions to actions_log table

Revision ID: 973c3ffd885a
Revises: fafeeb74ccc1
Create Date: 2025-10-27 15:12:12.895469

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '973c3ffd885a'
down_revision: Union[str, Sequence[str], None] = '9d0f51dc1dc7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    actions_table = sa.table('actions_log',
        sa.column('id', sa.Integer),
        sa.column('action', sa.String),
        sa.column('description', sa.String)
    )

    op.bulk_insert(actions_table,
        [
            {'id': 1, 'action': 'Responder Encuesta', 'description': 'Acción de responder una encuesta.'},
            {'id': 2, 'action': 'Aprobar/Rechazar Encuesta', 'description': 'Acción de aceptar o rechazar una encuesta por parte del administrador.'}
        ],
        multiinsert=False
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DELETE FROM actions_log WHERE id IN (1, 2)")
