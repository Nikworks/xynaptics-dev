"""Add Alert Hash to LastAlert

Revision ID: 55cc64020f6d
Revises: c6e5594c99f8
Create Date: 2024-12-08 16:24:01.808208

"""

import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision = "55cc64020f6d"
down_revision = "c6e5594c99f8"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("lastalert", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("alert_hash", sqlmodel.sql.sqltypes.AutoString(), nullable=True)
        )
        batch_op.create_index(
            batch_op.f("ix_lastalert_alert_hash"), ["alert_hash"], unique=False
        )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("lastalert", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_lastalert_alert_hash"))
        batch_op.drop_column("alert_hash")
    # ### end Alembic commands ###