"""adding first and second names to user

Revision ID: 711df8a9a6bd
Revises: 0d257d5c03b1
Create Date: 2020-03-26 00:59:56.672228

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '711df8a9a6bd'
down_revision = '0d257d5c03b1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('user', sa.Column('link_id', sa.String(120)))
    op.add_column('user', sa.Column('first_name', sa.String(80)))
    op.add_column('user', sa.Column('second_name', sa.String(80)))


def downgrade():
    op.drop_column('user', sa.Column('link_id', sa.String(120)))
    op.drop_column('user', sa.Column('first_name', sa.String(80)))
    op.drop_column('user', sa.Column('second_name', sa.String(80)))
