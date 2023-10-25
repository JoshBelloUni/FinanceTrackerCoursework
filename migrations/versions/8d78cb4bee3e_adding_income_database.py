"""adding income database

Revision ID: 8d78cb4bee3e
Revises: f48b895e5d33
Create Date: 2023-10-23 13:04:56.913624

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d78cb4bee3e'
down_revision = 'f48b895e5d33'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('incomes',
    sa.Column('Income_id', sa.INTEGER(), nullable=False),
    sa.Column('type', sa.VARCHAR(length=500), nullable=True),
    sa.Column('cost', sa.FLOAT(), nullable=True),
    sa.Column('date', sa.DATE(), nullable=True),
    sa.PrimaryKeyConstraint('Income_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('expenses',
    sa.Column('Expense_id', sa.INTEGER(), nullable=False),
    sa.Column('type', sa.VARCHAR(length=500), nullable=True),
    sa.Column('cost', sa.FLOAT(), nullable=True),
    sa.Column('date', sa.DATE(), nullable=True),
    sa.PrimaryKeyConstraint('Expense_id')
    )
    # ### end Alembic commands ###