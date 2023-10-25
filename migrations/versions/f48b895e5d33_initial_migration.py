"""initial migration

Revision ID: f48b895e5d33
Revises: 
Create Date: 2023-10-18 13:04:57.374908

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f48b895e5d33'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('expenses',
    sa.Column('Expense_id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=500), nullable=True),
    sa.Column('cost', sa.Float(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('Expense_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('expenses')
    # ### end Alembic commands ###