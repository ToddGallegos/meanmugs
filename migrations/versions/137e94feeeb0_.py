"""empty message

Revision ID: 137e94feeeb0
Revises: be22efe8840f
Create Date: 2023-02-15 02:53:07.418422

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '137e94feeeb0'
down_revision = 'be22efe8840f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('apitoken', sa.String(length=500), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('apitoken')

    # ### end Alembic commands ###
