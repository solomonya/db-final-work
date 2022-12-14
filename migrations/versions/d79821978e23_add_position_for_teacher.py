"""add position for teacher

Revision ID: d79821978e23
Revises: a64d5b84ac99
Create Date: 2022-11-16 16:19:02.961329

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = 'd79821978e23'
down_revision = 'a64d5b84ac99'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('teacher', sa.Column('position', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('teacher', 'position')
    # ### end Alembic commands ###
