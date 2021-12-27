"""empty message

Revision ID: bc0954824222
Revises: 3cefedaac148
Create Date: 2021-12-21 19:20:57.343253

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc0954824222'
down_revision = '3cefedaac148'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees_on_contracts',
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.Column('contract_id', sa.Integer(), nullable=False),
    sa.Column('labor_cat_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['contract_id'], ['contracts.id'], ),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], ),
    sa.ForeignKeyConstraint(['labor_cat_id'], ['labor_categories.id'], ),
    sa.PrimaryKeyConstraint('employee_id', 'contract_id', 'labor_cat_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employees_on_contracts')
    # ### end Alembic commands ###
